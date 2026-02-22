text = input("Enter text: ")

cleaned = text.lower().strip()
cleaned = " ".join(cleaned.split())

print("Cleaned text:", cleaned)
