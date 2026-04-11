#append().....add an element to the end of a list
#extend().....add multiple elements to the end of a list
#insert().....add an element at a specific index in a list
#remove().....remove the first occurrence of an element from a list
#pop().....remove and return the last element from a list
#clear().....remove all elements from a list
#index().....find the index of the first occurrence of an element in a list
#count().....count the number of occurrences of an element in a list
#sort().....sort the elements of a list in ascending order
#reverse().....reverse the order of the elements in a list
#copy().....create a copy of a list
#len().....return the number of elements in a list
#sum().....return the sum of all elements in a list (only for numeric lists)
my_list = [3, 1, 4, 1, 5, 9]
my_list.append(2)  # add an element to the end of the list
print(my_list)
my_list.extend([6, 5])  # add multiple elements to the end of the
list
print(my_list)
my_list.insert(0, 0)  # add an element at index 0
print(my_list)
my_list.remove(1)  # remove the first occurrence of 1
print(my_list)
popped_element = my_list.pop()  # remove and return the last element
print(popped_element)
print(my_list)
my_list.clear()  # remove all elements from the list
print(my_list)
my_list = [3, 1, 4, 1, 5, 9]
index_of_4 = my_list.index(4)  # find the index of the first occurrence of 4
print(index_of_4)
count_of_1 = my_list.count(1)  # count the number of occurrences of 1
print(count_of_1)
my_list.sort()  # sort the elements of the list in ascending order
print(my_list)
my_list.reverse()  # reverse the order of the elements in the list
print(my_list)
copied_list = my_list.copy()  # create a copy of the list
print(copied_list)
length_of_list = len(my_list)  # return the number of elements in the list
print(length_of_list)
sum_of_list = sum(my_list)  # return the sum of all elements in the list
print(sum_of_list)
