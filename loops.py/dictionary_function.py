#dict[key]....direct value ko access krne ke liye
student = {"name": "Vishakha", "age": 25, "city": "Indore"}
print(student["name"]) #direct value ko access krne ke liye
print(student.get("age")) #direct value ko access krne ke liye, agar key nahi milta hai to None return karega
print(student.get("country", "Not Found")) #agar key nahi milta hai to "Not Found" return karega

#dict.keys()....dictionary ke sare keys ko return karega
#dict.values()....dictionary ke sare values ko return karega

#pop()....dictionary se key-value pair ko remove karne ke liye
#popitem()....dictionary se last key-value pair ko remove karne ke liye
removed_value = student.pop("city")
print(removed_value) #remove kiya hua value print karega
print(student) #updated dictionary print karega

#del keyword....dictionary se key-value pair ko remove karne ke liye
del student["age"]
print(student) #updated dictionary print karega

#keys()....dictionary ke sare keys ko return karega
#values()....dictionary ke sare values ko return karega
#items()....dictionary ke sare key-value pairs ko return karega as a list of tuples
keys = student.keys()
print(keys) #dictionary ke sare keys print karega

#update()....dictionary me naye key-value pair add karne ke liye ya existing key ka value update karne ke liye
student.update({"country": "India"}) #naya key-value pair add karega
print(student) #updated dictionary print karega
student.update({"name": "Vishakha Patidar"}) #existing key ka value update
print(student) #updated dictionary print karega

#copy()....dictionary ka shallow copy banane ke liye
student_copy = student.copy()
print(student_copy) #copied dictionary print karega
#clear()....dictionary ke sare key-value pairs ko remove karne ke liye
student.clear()
print(student) #empty dictionary print karega

#in operator....dictionary me key ke presence ko check karne ke liye
is_name_present = "name" in student_copy
print(is_name_present) #True print karega kyunki "name" key student_copy me present hai
