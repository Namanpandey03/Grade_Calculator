name_of_student=input("enter students name: ")
try:
	chemistry=float(input("enter chemistry score: "))
	biology=float(input("enter biology score: "))
	physics=float(input("enter physics score: "))
	maths=float(input("enter maths score: "))
	history=float(input("enter history score: "))
	geography=float(input("enter geography score: "))
except ValueError:
	print("invalid input! please enter a number")
	exit()
passing_marks=40
total_marks=(chemistry+biology+biology+physics+maths+history+geography)
average_score=(total_marks/6)
print (f"Student's name - {name_of_student}")
print(f"chemistry: {chemistry: .2f}")
print(f"biology: {biology: .2f}")
print(f"physics: {physics: .2f}")
print(f"maths: {maths: .2f}")
print(f"history: {history: .2f}")
print(f"geography: {geography: .2f}")
print(f"total marks = {total_marks: .2f} / 600")
print(f"average score = {average_score: .2f}")
print("-----grade-----")
if average_score>=90:
	print("A+")
elif average_score>=80:
	print("A")
elif average_score>=70:
	print("B")
elif average_score>=60:
	print("C")
elif average_score>=50:
	print("D")
elif average_score>=40:
	print("E")
else:
	print("F")
compartment_subjects = []
if chemistry<passing_marks:
	compartment_subjects.append("chemistry")
if biology<passing_marks:
	compartment_subjects.append("biology")
if physics<passing_marks:
	compartment_subjects.append("physics")
if maths<passing_marks:
	compartment_subjects.append("maths")
if history<passing_marks:
	compartment_subjects.append("history")
if geography<passing_marks:
	compartment_subjects.append("geography")
if compartment_subjects:
	print(f"compartment in: {','.join(compartment_subjects)}")
else:
	print("no compartments")