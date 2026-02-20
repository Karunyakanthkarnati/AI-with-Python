marks = {}

marks["math"] = int(input("Enter math marks: "))
marks["science"] = int(input("Enter science marks: "))
marks["english"] = int(input("Enter english marks: "))

avg = (marks["math"] + marks["science"] + marks["english"]) / 3
marks["average"] = avg

print(marks)
