with open('sample.txt','r') as file:
    text = file.read()
    text = text.lower()
    words = text.split()
    print(f"The number of words in the file is: {len(words)}")
