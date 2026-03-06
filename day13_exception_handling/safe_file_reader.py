try:
    file = input("Enter the file name: ")
    with open(file,"r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")