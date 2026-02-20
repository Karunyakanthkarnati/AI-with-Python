student = {}
student["name"] = input("Enter your name: ")
student["marks"] = int(input("Enter your marks:"))
if student["marks"] > 35:
    student["result"] = 'pass'
else :
    student["result"] = 'fail'
print(student)
