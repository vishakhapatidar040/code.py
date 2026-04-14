tup = (2, 1, 3, 1)
print(type(tup))  # Output: <class 'tuple'>
print(tup[0])  # Output: 2
print(tup[1])  # Output: 1
print(tup[2])  # Output: 3
print(tup[3])  # Output: 1

# Tuples are immutable, so the following line will raise a TypeError
tup[0] = 5  # This will raise a TypeError because tuples are immutable