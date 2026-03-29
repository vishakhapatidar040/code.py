#function define (simple function)
#is  fuunction ka use same code ko bar bar likhne se bachne ke liye kiya jata hai.
#user define function banane ke liye hum 'def' keyword ka use karte hain, uske baad function ka naam aur parentheses me parameters (agar koi ho) likhte hain. Function body me wo code hota hai jo function call hone par execute hota hai. Function ko call karne ke liye hum function ka naam aur parentheses me arguments (agar koi ho) likhte hain.
def greet(name): #function header
    print("Hello, " + name + ". How are you?") #function body
 
greet("Gunjan patidar") #output: Hello, Gunjan patidar. How are you? 
greet("vishakha patidar") #output: Hello, vishakha patidar. How are you?
greet("neelam patidar") #output: Hello, neelam patidar. How are you?
greet("divya patidar") #output: Hello, divya patidar. How are you?
greet("neelam rajput") #output: Hello, neelam rajput. How are you?

#function with return statement(return value)
def add(a, b):
    return a + b
result = add(5, 3) #function call
print(result) #output: 8




#function with default parameter(default value)
def greet(name="Guest"):
    print("Hello, " + name + ". How are you?")
greet() #output: Hello, Guest. How are you?
greet("Gunjan patidar") #output: Hello, Gunjan patidar. How are you?

#function with parameter
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5  #input value
area = calculate_area(radius) #function call
print("Area of the circle with radius", radius, "is", area) #output: Area of the circle with radius 5 is 78.5

#function with multiple parameters
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = 43 #input weight in kg
height = 1.6002  #input height in meters
bmi = calculate_bmi(weight, height) #function call
print("Your BMI is:", bmi) #output: Your BMI is: 16.796875000000004

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
category = bmi_category(bmi) #function call
print("Your BMI category is:", category) #output: Your BMI category is: Underweight

#function with variable number of arguments
def calculate_average(*numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
avg = calculate_average(10, 20, 30) #function call
print("The average is:", avg) #output: The average is: 20.0
