def add(number1,number2):
 print(number1 + number2)
def sub(number1,number2):
 print(number1 - number2)
def mul(number1,number2):
 print(number1 * number2)
def div(number1,number2):
 print(number1 // number2)

number1 = int(input("Enter value for number 1 : "))
number2 = int(input("Enter value for number 2 : "))

print(f"""
         1. Addition
         2. Subtraction
         3. Multiplication
         4. Division
      """)
choice = int(input("Enter your choice : "))

if choice == 1:
    add(number1,number2)
elif choice == 2:
    sub(number1,number2)
elif choice == 3:
    mul(number1,number2)
elif choice == 4:
    div(number1,number2)
else:
   print("PLease choose correct option")