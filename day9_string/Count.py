text = input("Enter text: ")
count = 0

for ch in text:
    if ch != " ":
        count += 1

print("Character count:", count)
