import argparse
import logging
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

import requests
from prettytable import PrettyTable
from requests.exceptions import ChunkedEncodingError, ConnectionError

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_RETRIES = 3  # Max retries for a failed chunk download


def download_chunk(url, start, end, chunk_id, output_file, max_speed, stats):
    """
    Download a chunk of the file using a specific byte range with retries.
    """
    headers = {"Range": f"bytes={start}-{end}"}
    retries = 0

    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, headers=headers, stream=True, timeout=10)
            if response.status_code == 206:  # Partial content
                with open(f"{output_file}.part{chunk_id}", "wb") as f:
                    chunk_size = 0
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        chunk_size += len(chunk)

                        # Update stats
                        stats["total_bytes"] += len(chunk)
                        stats["total_packets"] += 1

                        # Apply max speed limit if set
                        if max_speed > 0:
                            time.sleep(chunk_size / max_speed)

                logging.debug(f"Chunk {chunk_id} downloaded successfully.")
                return  # Exit the function after a successful download
            else:
                logging.error(f"Error downloading chunk {chunk_id}. Status code: {response.status_code}")
                break
        except (ChunkedEncodingError, ConnectionError) as e:
            retries += 1
            logging.warning(f"Error downloading chunk {chunk_id}. Retrying {retries}/{MAX_RETRIES}... ({str(e)})")
            time.sleep(2)
        except Exception as e:
            logging.error(f"Unexpected error downloading chunk {chunk_id}: {str(e)}")
            break

    logging.error(f"Failed to download chunk {chunk_id} after {MAX_RETRIES} retries.")


def merge_chunks(output_file, num_chunks, directory):
    """Merge all downloaded chunks into one file."""
    with open(output_file, "wb") as final_file:
        for chunk_id in range(num_chunks):
            part_filename = os.path.join(directory, f"{output_file}.part{chunk_id}")
            with open(part_filename, "rb") as part_file:
                final_file.write(part_file.read())
            os.remove(part_filename)
    logging.debug(f"Chunks merged into {output_file}")


def update_stats_table(stats, total_size, table, file_name):
    """Update stats table periodically."""
    last_downloaded = stats["total_bytes"]
    last_time = time.time()

    while stats["total_bytes"] < total_size:
        # Calculate elapsed time, download speed, and ETA
        elapsed_time = time.time() - stats["start_time"]
        elapsed_minutes = elapsed_time / 60

        current_time = time.time()
        current_downloaded = stats["total_bytes"]
        download_speed = (current_downloaded - last_downloaded) / (current_time - last_time) if current_time - last_time > 0 else 0
        last_time = current_time
        last_downloaded = current_downloaded

        eta = (total_size - stats["total_bytes"]) / download_speed if download_speed > 0 else 0
        eta_minutes = eta / 60

        percentage = (stats["total_bytes"] / total_size) * 100

        # Update table
        table.clear_rows()
        table.add_row(["File Name", file_name])
        table.add_row(["Total Bytes", f"{stats['total_bytes'] / (1024 * 1024):.2f} MB"])
        table.add_row(["Packets", stats["total_packets"]])
        table.add_row(["Loss", stats["total_loss"]])
        table.add_row(["Elapsed", f"{elapsed_minutes:.2f} min"])
        table.add_row(["Speed", f"{download_speed / (1024 * 1024):.2f} MB/s"])
        table.add_row(["ETA", f"{eta_minutes:.2f} min"])
        table.add_row(["Percentage", f"{percentage:.2f}%"])

        print("\033c", end="")
        print(table)

        time.sleep(1)  # Update every 1 second


def download_file(url, output_file, num_connections, max_speed, split, directory):
    """Download a file using multiple connections and manage chunk downloading."""
    # Fetch file size and calculate chunk sizes
    response = requests.head(url)
    total_size = int(response.headers["Content-Length"])
    chunk_size = total_size // num_connections

    # Initialize stats dictionary
    stats = {"total_bytes": 0, "total_packets": 0, "total_loss": 0, "start_time": time.time()}

    # Initialize the PrettyTable
    table = PrettyTable()
    table.field_names = ["Metric", "Value"]

    # Use ThreadPoolExecutor for managing threads
    with ThreadPoolExecutor(max_workers=num_connections) as executor:
        futures = []
        for i in range(num_connections):
            start = i * chunk_size
            end = (i + 1) * chunk_size - 1 if i < num_connections - 1 else total_size
            futures.append(executor.submit(download_chunk, url, start, end, i, os.path.join(directory, output_file),
                                           max_speed, stats))

        # Start updating the stats table in a separate thread
        stats_thread = threading.Thread(target=update_stats_table, args=(stats, total_size, table, output_file))
        stats_thread.start()

        # Wait for all download threads to finish
        for future in futures:
            future.result()

        # Merge downloaded chunks into the final file
        merge_chunks(output_file, num_connections, directory)

        # Wait for the stats table to finish
        stats_thread.join()

        # Final table update
        elapsed_time = time.time() - stats["start_time"]
        elapsed_minutes = elapsed_time / 60

        table.clear_rows()
        table.add_row(["File Name", output_file])
        table.add_row(["Total Bytes", f"{stats['total_bytes'] / (1024 * 1024):.2f} MB"])
        table.add_row(["Packets", stats["total_packets"]])
        table.add_row(["Loss", stats["total_loss"]])
        table.add_row(["Elapsed", f"{elapsed_minutes:.2f} min"])

        print(table)


def get_file_name_from_url(url):
    """Extract the file name from the URL."""
    return os.path.basename(urlparse(url).path)


def main():
    """Main function to handle command-line arguments and download the file."""
    parser = argparse.ArgumentParser(description="Download a file using a custom downloader.")
    parser.add_argument("-u", "--url", required=True, help="URL of the file to download")
    parser.add_argument("-o", "--output", required=False, help="Output file name")
    parser.add_argument("-d", "--directory", required=False, default=".", help="Directory to save the downloaded file")
    parser.add_argument("-x", "--max-connections", type=int, default=16, help="Maximum number of connections (default: 16)")
    parser.add_argument("-s", "--split", type=int, default=10, help="Number of chunks to split the download into (default: 10)")
    parser.add_argument("-m", "--max-speed", type=int, default=0, help="Maximum download speed in bytes per second (default: 0, no limit)")

    args = parser.parse_args()

    # Validate URL
    if not args.url.startswith("http"):
        print("Invalid URL. Please provide a valid HTTP/HTTPS URL.")
        return

    # Output file name and directory
    output_file = args.output or get_file_name_from_url(args.url)
    directory = args.directory

    # Ensure the output directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    logging.info(f"Starting download of {output_file} from {args.url}")

    # Start downloading the file
    download_file(args.url, output_file, args.max_connections, args.max_speed, args.split, directory)
    logging.info(f"Download complete. File saved as {output_file}.")


if __name__ == "__main__":
    main()
