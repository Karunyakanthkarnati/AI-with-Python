text = "Hello Guys... Today is our annual day. Is   Every one Exicted????     "
text = text.lower()
text = text.replace(".","")
text = text.replace("?","")
words = text.split()
print(text)
print(f'No.of words are {len(words)}')
