with open('sample.txt','r') as file:
    text = file.read()
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split()
    unique_words = set(words)
with open('analysis_report.txt', 'w') as report:
    report.write(
        f"--- FILE ANALYSIS REPORT ---\n"
        f"Total Words: {len(words)}\n"
        f"Unique Words: {len(unique_words)}\n"
        f"----------------------------\n"
    )
