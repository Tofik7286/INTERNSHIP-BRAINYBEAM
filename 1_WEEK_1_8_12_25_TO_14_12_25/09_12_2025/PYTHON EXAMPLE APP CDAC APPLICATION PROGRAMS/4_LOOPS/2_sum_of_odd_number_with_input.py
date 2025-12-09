sum = 0
number = int(input("Enter Number : "))


print("""
      --------------
        Odd Sum 
      --------------
""")
for i in range(1,number+1):
    if i % 2 == 1:
        print(i,end=",")
        sum += i
print("Sum of odd number : ",sum)

print("""
      --------------
        Even Sum 
      --------------
""")

sum = 0
for i in range(1,number+1):
    if i % 2 == 0:
        print(i,end=",")
        sum += i
print("Sum of even number : ",sum)
