number = int(input("Enter Number : "))
sum = 0
for i in range(1,number+1):
    print(i,end=",")
    sum += i
print("Sum is : ",sum)