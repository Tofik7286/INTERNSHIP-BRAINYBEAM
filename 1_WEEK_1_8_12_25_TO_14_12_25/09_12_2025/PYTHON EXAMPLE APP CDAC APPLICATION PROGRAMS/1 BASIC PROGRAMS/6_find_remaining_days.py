days = int(input("Enter total days : "))
year = days//365
remaining_days = days % 365
month = remaining_days // 30
remaining_days = remaining_days % 30

print(f'''
    Remaining 
    Year : {year}
    Month : {month}
    Days : {remaining_days}
''')