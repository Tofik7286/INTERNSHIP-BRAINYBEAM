roll_no = int(input("Enter Roll no : "))
math = int(input("Enter Math marks : "))
science = int(input("Enter Science marks : "))
english = int(input("Enter English marks : "))

total = math + science + english

print(f'''
    Roll No : {roll_no}
    Math : {math}
    Science : {science}
    English : {english}
    Total : {total}
    Average : {total / 3}
''')