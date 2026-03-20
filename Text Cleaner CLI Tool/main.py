import string

try:
    filename = input("Enter the file path: ")

    with open(filename) as file:
        text = file.read()

    text = text.lower()
    text = text.strip()

    for char in string.punctuation:
        text = text.replace(char, "")

    words = text.split()

    total_words = len(words)
    unique_words = len(set(words))

    cleaned_text = " ".join(words)

    with open("cleaned_text.txt", "w") as output:
        output.write(cleaned_text)

    with open("analysis_report.txt", "w") as report:
        report.write(
            f"--- FILE ANALYSIS REPORT ---\n"
            f"Total Words: {total_words}\n"
            f"Unique Words: {unique_words}\n"
            f"----------------------------\n"
        )

    print("File processed successfully.")
    print(f"Total Words: {total_words}")
    print(f"Unique Words: {unique_words}")

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

except Exception as e:
    print(f"An error occurred: {e}")