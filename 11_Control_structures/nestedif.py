
mark=int(input("Enter your marks: "))

if mark>40 and mark<=100:
	if mark>=40 and mark<50:
		print("Grade D")
	elif mark>=50 and mark<60:
		pass
	elif mark>=60 and mark<70:
		print("Grade B")
	elif mark>=70 and mark<80:
		print("Grade A")
	else:
		pass

else:
	print("Fail")
