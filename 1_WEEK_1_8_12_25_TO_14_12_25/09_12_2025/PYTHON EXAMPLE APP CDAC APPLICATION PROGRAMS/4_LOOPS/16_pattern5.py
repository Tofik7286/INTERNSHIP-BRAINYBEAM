n = int(input("Enter Number : "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print("---------------------------")
for i in range(1 , n+1):
    for j in range(i , n+1 ):
        print(j,end=" ")
    print()

print("---------------------------")

for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=" ")
    print()

print("---------------------------")
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    