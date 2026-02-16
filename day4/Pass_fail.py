def result(name,marks):
    if marks >= 40:
        return f"{name} has passed"
    else:
        return f"{name} has failed"
       
name = input("Enter your name : ")
marks = int(input("Enter your marks : "))
print(result(name,marks))
