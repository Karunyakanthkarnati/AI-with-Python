import random
import string
n = int(input("Enter the length of password :"))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(n):
    password += random.choice(characters)
print(f"The generated password is : {password}")