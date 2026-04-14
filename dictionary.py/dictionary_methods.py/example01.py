info = {"name":"Vishakha Patidar",
        "age": 19,
        "favorite_color": "light blue",
        "hobbies": ["coding", "painting", "traveling"],
        "father_name": "Mahesh Patidar"
        }
print(info) 

print(list(info.keys())) #printing all the keys of the dictionary

info.keys()
print(info.keys()) #printing all the keys of the dictionary

info.values()
print(info.values()) #printing all the values of the dictionary

info.items()
print(info.items()) #printing all the key-value pairs of the dictionary

info.get("name")
print(info.get("name")) #printing the value of the key "name"

info.update({"mother_name": "Seema Patidar"})
print(info) #printing the updated dictionary with the new key-value pair

info.setdefault("age", 20)
print(info) #printing the dictionary after using setdefault method to update the value of the key "age"

info.pop("favorite_color")
print(info) #printing the dictionary after removing the key "favorite_color" using pop method

info.clear()
print(info) #printing the dictionary after clearing all the key-value pairs using clear method