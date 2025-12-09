# 1. Print a Hello message on interactive screen.

# print("Hello")

# 2. Create a Python program to demonstrate the use of comments(single and multi-line).


# This is single line

'''
    this is multi 
    line comment
'''

# 3. Create a Python program that will have 3 variables which stores integer, float and complex value. Display its value and also demonstrate its datatype class using type().


integer_variable = 10
float_variable = 365.45

x = 10
y = 20
complex_variable =  10+2j

'''
print(f"""
    integer value : {integer_variable}, type : {type(integer_variable)}
    float value : {float_variable}, type : {type(float_variable)}
    complex value : {complex_variable}, type : {type(complex_variable)}
""")
'''
# 4. Create a Python program that will have one string variable =“Welcome to Python”.
# Perform following operations:
# • Print whole string
# • Print only first character of string
# • Print 3rdcharacter to -1 character of string using slicing operator
# • Print string from 4thcharacter to the end of string using slicing operator
# • Print whole string 5 times using appropriate operator.

str = "Welcome to Python"

# print(str)
# print(str[0])
# print(str[3:-1])
# print(str[4:])
# print(str*4)


# 5. Create a Python program that will have one list with values = [‘Navratri’, ‘Diwali’, ‘Holi’, ‘Rakshabandhan’,’Bakri Id’, ‘Muharram’ ]. Perform following operations:
# • Print whole list
# • Print only first element of list
# • Prints elements starting from 2nd till 3rd
# • Prints elements starting from 2nd element till last
# • Print whole list 4 times using appropriate operator.

festivals = ['Navratri', 'Diwali','Holi','Rakshabandhan','Bakri Eid','Muharram']

# print(festivals)
# print(festivals[0])
# print(festivals[2:4])
# print(festivals[2:])
# print(festivals*4)


# 6. Create a Python program that will have one fruit dictionary with fruit values. Display keys and values separately.

fruit = {
    "Apple" : "Apple is healthy fruit",
    "Orange" : "Orange has rich vitamin C",
}

# for key in fruit:
#     print(f"{key} : {fruit[key]}")

# 7. Create a Python program that will have one tuple of vegetables with values = (‘Potato’,‘Brinjal’,‘Tomato’,‘Cabbage’, ‘Cauliflower’). Perform following operations:
# • Print whole tuple
# • Print only first element of tuple
# • Prints elements starting from 2nd till 4th
# • Prints elements starting from 2nd element till last
# • Print whole tuple twice using appropriate operator.
