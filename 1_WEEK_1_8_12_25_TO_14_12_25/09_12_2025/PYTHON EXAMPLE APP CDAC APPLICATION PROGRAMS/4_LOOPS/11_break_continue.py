#break

number = int(input("Enter Number : "))
for i in range(1,number+1):
    if i == 4:
      break
    else:
       print(i,end=",")
#continue

number = int(input("Enter Number : "))
for i in range(1,number+1):
    if i == 4:
      continue
    else:
       print(i,end=",")
