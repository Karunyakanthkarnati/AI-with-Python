text = input("Enter the text : ")
cleaned_text = text.strip().lower()
words = cleaned_text.split()
unique_words = set(words)
print(f"""--- TEXT ANALYSIS REPORT ---
Cleaned Text: {cleaned_text}
Total Words: {len(words)}
Unique Words: {len(unique_words)}
----------------------------""")
