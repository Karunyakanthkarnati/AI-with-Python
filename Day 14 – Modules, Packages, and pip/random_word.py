import random
text = input("Enter the text : ")
words = text.split()
selected_text = random.choice(words)
print(f"The randomly selected word is {selected_text}")