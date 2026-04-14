set = {1, 2, 3, 4 }
set.add(5) # adds 5 to the set
print(set) # Output: {1, 2, 3, 4, 5}

set.remove(3) #3 ko hta dega, agr 3 set me nhi h to error aayega
print(set) # Output: {1, 2, 4, 5}

set.discard(2) #2 ko remove krega
print(set) # Output: {1, 4, 5}

#agr set me 2 nhi h to error ni aayega discart method me

set.pop() #randomly ek element ko remove krta hai
print(set)

set.clear() #set ko empty kr deta hai
print(set) # Output: set()