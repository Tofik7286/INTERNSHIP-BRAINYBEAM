number = int(input("Enter Number : "))
flag = False
for i in range(2,number):
    if number % i==0:
        flag = True
        break
    else:
        flag = False

if flag:
    print(f"{number} is not prime")
else:
    print(f"{number} is  prime")