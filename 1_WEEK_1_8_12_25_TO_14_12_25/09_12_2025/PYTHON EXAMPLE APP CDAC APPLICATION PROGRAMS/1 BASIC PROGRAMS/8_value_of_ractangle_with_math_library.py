import math
r = float(input("Enter Radius of Circle : "))
r =round(r,2)
a = math.pi*r*r
a = round(a,2)
print(f'''
    Radius of circle : {r}
    Area of circle : {a}
''')