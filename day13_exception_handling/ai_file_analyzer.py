try:
    filename = input("Enter the file name : ")
    with open(filename ,'r') as file:
        text = file.read()
    text = text.lower()
    text = text.strip()
    text = text.replace("."," ").replace(","," ").replace("/"," ").replace("?"," ").replace("!"," ").replace(";"," ").replace(":"," ")
    words = text.split()
    unique = set(words)
    print(f"Total no.of words are : {len(words)}")
    print(f"Total no.of unique words are : {len(unique)}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:      
    print(f"An error occurred: {e}")
with open("Output.txt","w") as file:
    file.write(f'''--- FILE ANALYSIS REPORT ---
    Total Words: {len(words)}
    Unique Words: {len(unique)}
----------------------------''')
