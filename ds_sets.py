user_id_list_1 = {424, 245, 432, 167, 731, 732, 145}
user_id_list_2 = {235, 32, 74, 689, 56, 35, 125}
user_id_list_3 = {34, 56, 78, 90, 12}

user_id_list = user_id_list_1.union(user_id_list_2).union(user_id_list_3)
print("User IDs: ", user_id_list)

# 3 sets of random cities
city_list_1 = {"New York", "Los Angeles", "Chicago", "Houston", "Phoenix"}
city_list_2 = {"Philadelphia", "San Antonio",
               "San Diego", "Dallas", "San Jose"}
city_list_3 = {"Austin", "Jacksonville",
               "Fort Worth", "Columbus", "San Francisco"}

city_list = city_list_1.union(city_list_2).union(city_list_3)
print("City list: ", city_list)

is_city_lists_disjoint = city_list_1.isdisjoint(
    city_list_2)
print("City lists are disjoint: ", is_city_lists_disjoint)


# 3 sets of random numbers for  intersection set
num_list_1 = {2, 5, 7, 1, 9, 10, 3}
num_list_2 = {4, 5, 6, 7}
num_list_3 = {1, 2, 3, 4, 5, 6, 7}

num_list = num_list_1.intersection(num_list_2).intersection(num_list_3)
print("Number list .intersection(set): ", num_list)

# .difference(set)

num_list_diff = num_list_1.difference(num_list_2)
print("Number list difference: ", num_list_diff)


num_list_superset = num_list_3.issuperset(num_list_2)
print("Number list is superset: ", num_list_superset)


num_list_subset = num_list_2.issubset(num_list_3)
print("Number list is subset: ", num_list_subset)
