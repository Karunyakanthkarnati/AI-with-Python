def age_details(name,year):
    age = 2026-year
    return age , age+10
name = input("enter your name : ")
year = int(input("enter your birth year : "))
present_age , future_age = age_details(name,year)
print(f"Hello {name}")
print(f"Your current age is {present_age}")
print(f"Your age after 10 years is {future_age}")
