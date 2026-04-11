#and function
x = 10
print(x > 5 and x < 15) #ye condition true hai
print(x > 5 and x < 10) #ye condition false hai

#or function
y = 20
print(y > 15 or y < 25) #ye condition true hai
print(y > 25 or y < 15) #ye condition false hai

#not function
z = 5
print(not z > 10) #ye condition true hai
print(not z < 10) #ye condition false hai

#combining logical functions
a = 8
b = 12
print((a > 5 and b < 15) or (a < 5 and b > 15)) #ye condition true hai
print((a > 10 and b < 5) or (a < 5 and b > 15)) #ye condition false hai

#logical functions can be used in if statements
if x > 5 and x < 15:
    print("x is between 5 and 15")
else:
    print("x is not between 5 and 15")

#all() function
numbers = [1, 2, 3, 4, 5]
print(all(num > 0 for num in numbers)) #ye condition true hai
print(all(num > 3 for num in numbers)) #ye condition false hai

#any() function
print(any(num > 4 for num in numbers)) #ye condition true hai
print(any(num > 5 for num in numbers)) #ye condition false hai

#comparison operators with logical functions
# == operator (equal to )
# != operator (not equal to)
# > < operators (greater than, less than)
# >= <= operators (greater than or equal to, less than or equal to)
# logical functions can be used to combine these operators for more complex conditions
#example:
age = 25   
if age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are not an adult.")
      