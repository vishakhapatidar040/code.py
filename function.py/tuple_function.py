#tuple function is immutable but agr change krna ho to list m convert krke change kr skte h
my_tuple = (1, 2, 3, 4, 5)
# Convert tuple to list
my_list = list(my_tuple)
# Modify the list
my_list[0] = 10
# Convert back to tuple
my_tuple = tuple(my_list)
print(my_tuple) #output: (10, 2, 3, 4, 5)

