
num_tup = (2, 5, 7, 1)
print(type(num_tup))
print(num_tup)

# add to tuple
num_tup = num_tup + (10, 15, 20)
print(num_tup)

# remove from tuple
num_tup = num_tup[:2] + num_tup[3:]
print(num_tup)


def add_to_tuple(tup: tuple, item) -> tuple:
    """#+
    This function adds an item to the end of a tuple.#+
#+
    Parameters:#+
    tup (tuple): The original tuple to which the item will be added.#+
    item (any): The item to be added to the tuple.#+
#+
    Returns:#+
    tuple: A new tuple with the item added to the end.#+
#+
    Raises:#+
    TypeError: If the input is not a tuple.#+
    """  # +
    if not isinstance(tup, tuple):
        raise TypeError(f"Expected tuple but got {type(tup).__name__}")
    temp_list = list(tup)
    temp_list.append(item)
    return tuple(temp_list)


print(add_to_tuple(num_tup, 100))
