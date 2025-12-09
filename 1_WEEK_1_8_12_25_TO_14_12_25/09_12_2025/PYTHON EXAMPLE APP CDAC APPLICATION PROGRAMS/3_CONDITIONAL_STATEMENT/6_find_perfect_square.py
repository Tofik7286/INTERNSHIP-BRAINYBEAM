import math
number = int(input("Enter NUmber : "))
s = int(math.sqrt(number))

if (number == s*s):
  print(f"{number} is perfect square root")
else:
  print(f"{number} is not perfect square root")