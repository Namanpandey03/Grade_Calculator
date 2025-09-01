import json
Student_name=input(f"Enter student name:")
try:
	num_subjects=int(input("enter no of subjects: "))
except ValueError:
	print("not a number,try again")
	exit()
subject_data=[]

for i in range(num_subjects):
	subject=input(f"\n subject name #{i+1}: ")
	try:
		marks=float(input(f"marks obtained {subject}: "))
	except ValueError:
		print("invalid marks , enter a numeric value")
		exit()
	subject_data.append({"subject": subject,"marks": marks})

	mark_list=[entry["marks"]for entry in subject_data]
	average= sum(mark_list)/len(mark_list)
	highest_marks=max(mark_list)
	lowest_marks=min(mark_list)

if average>=90:
	grade = "A++"
elif average>=85:
	grade = "A"
elif average>=80:
	grade = "B"
elif average>=70:
	grade = "C"
elif average>=60:
	grade = "D"
elif average>=50:
	grade = "E"
else:
	grade = "fail"

print("-----grade summary-----")
for entry in subject_data:
	print(f"{entry['subject']} : {entry['marks']}")
	print(f"\n average: {average:.2f}")
	print(f"\n highest marks: {highest_marks}")
	print(f"\n lowest marks: {lowest_marks}")
	print(f"\n final grade: {grade}") 

save= input("\ndo you want to save this? (yes/no):").lower()
if save==("yes"):
	with open("grade_summary.json","w") as f:
		summary = {
			"student": Student_name,
			"subjects": subject_data,
			"average": round(average,2),
			"highest": highest_marks,
			"lowest": lowest_marks,
			"final_grade": grade
		}
		json.dump(summary,f,indent=4)
		print("Results saved to 'grade_summary.json' ")