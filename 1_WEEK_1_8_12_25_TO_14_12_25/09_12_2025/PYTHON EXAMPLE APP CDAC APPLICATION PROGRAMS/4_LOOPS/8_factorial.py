number = int(input("Enter Number : "))
mul = 1

if number <=0:
    print("We can not perform factorial on zero or negative number")
else:
    for i in range(1,number + 1):
        mul = mul * i
print(f"Factorial is : {mul}")