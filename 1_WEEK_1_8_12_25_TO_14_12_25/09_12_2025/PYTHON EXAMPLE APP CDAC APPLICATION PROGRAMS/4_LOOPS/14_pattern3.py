n = int(input("Enter Number : "))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(i,end="")
    print()

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end="")
    print()