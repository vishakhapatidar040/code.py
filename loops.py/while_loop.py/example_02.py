#print numbers from 1 to 5
i = 1
while i<=5: #infinite loop nhi banana hai always use <= or >= condition in while loop
    print(i)
    i += 1
print("loop ended")
#print numbers from 5 to 1
#we can also use while loop to print numbers in reverse order
#we will start with 5 and decrement the value of i in each iteration
i = 5
while i>=1: #avoid using i>0 condition because it will print 0 as well as it will be true for i=0
    print(i)
    i -= 1
print("loop ended")
