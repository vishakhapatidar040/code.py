#lower().....small letters
#upper().....capital letters
#title().....first letter of each word is capital
#capitalize().....first letter of the string is capital
#strip().....remove spaces from the beginning and end of the string
#lstrip().....remove spaces from the beginning of the string
#rstrip().....remove spaces from the end of the string
#replace().....replace a part of the string with another string
#split().....split the string into a list of substrings based on a specified delimiter
#join().....join a list of strings into a single string with a specified delimiter
#find().....find the index of the first occurrence of a substring in a string
#count().....count the number of occurrences of a substring in a string
#startswith().....check if a string starts with a specified substring
#endswith().....check if a string ends with a specified substring
#isalpha().....check if all characters in a string are alphabetic
#isdigit().....check if all characters in a string are digits
#isspace().....check if all characters in a string are whitespace
#len().....length of the string
#indexing and slicing.....accessing specific characters or substrings in a string using their index positions
#concatenation.....combining two or more strings together using the + operator
#repetition.....repeating a string multiple times using the * operator

v = "Hello World I am Vishakha Patidar and I am learning Python"
print(v.lower()) #small letters
print(v.upper()) #capital letters pura string capital me convert ho jayega
print(v.title()) #har word ka first letter capital me convert ho jayega
print(v.capitalize()) #sirf first letter of the string capital me convert ho jayega baki sab small me convert ho jayega
print(v.strip()) #string ke beginning aur end me jo spaces h unko remove kr dega
print(v.lstrip()) #left side ke spaces ko remove kr dega
print(v.rstrip()) #right side ke spaces ko remove kr dega
print(v.replace("Vishakha", "Vishu")) #string me jo "Vishakha" h usko "Vishu"se replace kr dega
print(v.split())   #string ko list me convert kr dega jaha pe space h waha pe split kr dega    
print("-".join(v.split())) #string ke har word ko join kr dega with a hyphen in between
print(v.find("Vishakha")) #string me "Vishakha" ka first occurrence ka index deg[a, agar sub]string nahi milta hai to -1 return karega
print(v.count("a")) #string me "a" ka kitne baar occurrence hai uska count dega
print(v.startswith("Hello")) #string check karega ki kya string "Hello" se start hota hai ya nahi, agar start hota hai to True return karega otherwise False return karega
print(v.endswith("Python")) #string check karega ki kya string "Python" se end hota hai ya nahi, agar end hota hai to True return karega otherwise False return karega
print(v.isalpha()) #string check karega ki kya string me sirf alphabetic characters hai ya nahi, agar sirf alphabetic characters hai to True return karega otherwise False return karega
print(v.isdigit()) #string check karega ki kya string me sirf digits hai ya nahi, agar sirf digits hai to True return karega otherwise False return karega
print(v.isspace()) #string check karega ki kya string me sirf whitespace characters hai ya nahi, agar sirf whitespace characters hai to True return karega otherwise False return karega
print(len(v)) #string ke length ko return karega, yani string me kitne characters hai including spaces
print(v[0])  # indexing
print(v[6:11])  # slicing
print(v + " and I am enjoying it")  # concatenation
print(v * 2)  # repetition
print(v[0:5].upper() + v[5:])  # combining indexing, slicing, and case change