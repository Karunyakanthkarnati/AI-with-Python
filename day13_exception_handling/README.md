# Day 13 – Exception Handling in Python (try / except)

This project demonstrates **exception handling in Python** to prevent programs from crashing due to unexpected errors.

Exception handling is essential for building **reliable software and AI systems**, where inputs, files, and external data sources may fail or behave unpredictably.

This day focuses on writing **safe Python programs** that continue running even when errors occur.

---

## 📌 Topics Covered

* What exceptions are
* Why programs crash
* Using `try` and `except`
* Handling specific errors (`ValueError`, `FileNotFoundError`)
* Handling unexpected errors using `Exception`
* Combining exception handling with file processing

---

## 🧠 Why Exception Handling Matters in AI

Real-world AI systems frequently encounter errors such as:

* Missing files
* Invalid user input
* Corrupted datasets
* API request failures
* Network interruptions

Without proper exception handling, these errors can **crash the entire pipeline**.

Using `try` / `except` ensures that systems remain **stable, predictable, and recoverable**.

---

## 🧪 Programs Included

### 1️⃣ easy_safe_number_input.py

A simple program that safely converts user input to an integer.

If the user enters invalid input, the program catches the error and displays a message instead of crashing.

---

### 2️⃣ medium_safe_file_reader.py

Reads a file provided by the user and displays its content.

Handled exceptions:

* `FileNotFoundError`
* Unexpected errors

---

### 3️⃣ hard_ai_file_analyzer.py

A more advanced program that:

1. Reads text from a file
2. Cleans the text
3. Splits the text into words
4. Counts total words
5. Calculates unique words
6. Saves an analysis report to an output file

This demonstrates **AI-style text preprocessing combined with error handling**.

---

## 📂 Project Structure

```
python-ai-exception-handling-day13
│
├── README.md
│
└── day13_exception_handling
    ├── easy_safe_number_input.py
    ├── medium_safe_file_reader.py
    └── hard_ai_file_analyzer.py
```

---

## 📊 Skills Demonstrated

* Python exception handling
* Safe user input processing
* File reading with error protection
* Text cleaning and preprocessing
* Word counting and vocabulary extraction
* Writing formatted reports to files

---

## 🎯 Learning Outcome

By completing Day 13, you can:

* Write Python programs that **do not crash on errors**
* Handle invalid input safely
* Build **robust file-processing scripts**
* Combine file handling with exception handling
* Design safer **data-processing pipelines for AI systems**

---