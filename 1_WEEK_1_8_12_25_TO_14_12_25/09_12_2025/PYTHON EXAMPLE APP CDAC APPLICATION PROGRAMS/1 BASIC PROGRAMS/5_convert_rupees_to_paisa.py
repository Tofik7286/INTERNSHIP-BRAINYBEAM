print("This program will give you rupees paisa and total amount")

amount = float(input("Enter Rupees and paisa : "))
rupees = int(amount)
paisa = int((amount - rupees) * 100)

print(f'''
    Your Original Amount : {amount}
    Rupees : {rupees}
    Paisa : {paisa}
''')