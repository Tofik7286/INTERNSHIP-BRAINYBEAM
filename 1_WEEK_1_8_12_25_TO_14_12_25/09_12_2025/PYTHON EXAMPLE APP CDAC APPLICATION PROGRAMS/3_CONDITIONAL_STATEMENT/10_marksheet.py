roll_no = int(input("Enter roll no : "))
c = int(input("Enter C marks : "))
java = int(input("Enter Java marks : "))
python = int(input("Enter Python marks :"))
total = c + java + python
per = round(float(total / 3),2)

print("Total : ",total)
print("Percentage : ",per)
if per <= 100 and per >= 85:
  print("Grade A")
elif per < 85 and per >= 70:
  print("Grade B")
elif per < 70 and per >= 50:
  print("Grade C")
elif per < 50 and per >= 35:
  print("Grade D")
else:
  print("Failed")