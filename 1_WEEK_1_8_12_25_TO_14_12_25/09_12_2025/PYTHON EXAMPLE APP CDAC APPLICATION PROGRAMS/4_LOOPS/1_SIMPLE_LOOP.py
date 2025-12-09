# 1 to 10
print("""
      -------------
        1 to 10
      -------------
      """)
for i in range(1,11):print(i)

print("""
      -------------
        10 to 1
      -------------
      """)
for i in range(10,0,-1):print(i)

print("""
      -------------
        1 to n
      -------------
      """)

n = int(input("Enter number : "))
for i in range(n+1):
    print(i)
print("""
      -------------
        n to 1
      -------------
      """)
# n = int(input("Enter number : "))
for i in range(n,0,-1):
    print(i)

print("""
      -------------
        n to m
      -------------
      """)

n = int(input("Enter n : "))
m = int(input("Enter m : "))
for i in range(n,m+1):
    print(i)