#create an empty list 
fruits = []

#take input from the user for 7 fruits and add them to the list
for i in range(7):
    fruit = input(f"Enter fruit {i+1}:")
    fruits.append(fruit)

    #Display the list of fruits
print("List of fruits :", fruits)