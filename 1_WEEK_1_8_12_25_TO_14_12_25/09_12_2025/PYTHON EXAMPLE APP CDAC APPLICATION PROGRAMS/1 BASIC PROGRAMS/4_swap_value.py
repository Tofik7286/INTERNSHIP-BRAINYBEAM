a = int(input("Enter value for a "))
b = int(input("Enter value for b "))


print(f'''
    Before Swapping : 
    A : {a}
    B : {b}
''')
# using 2 variable

a,b = b,a 

print(f'''
    After Swapping : 
    A : {a}
    B : {b}
''')



a = a+b
b = a-b
a = a-b


print(f'''
    After Swapping : 
    A : {a}
    B : {b}
''')
