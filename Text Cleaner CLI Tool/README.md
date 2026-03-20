# Text Cleaner CLI Tool (Day 15)

This project is a **command-line tool (CLI)** built using Python to clean and analyze text files.
It simulates the **text preprocessing stage used in AI and NLP pipelines**.

---

## 🧠 Project Overview

Raw text data often contains:

* uppercase/lowercase inconsistencies
* punctuation noise
* irregular spacing

Before feeding text into AI models, it must be **cleaned and standardized**.

This tool performs:

* text normalization
* punctuation removal
* word tokenization
* basic text analysis

---

## 🚀 Features

* Reads text from a user-provided file
* Converts text to lowercase
* Removes punctuation
* Splits text into words
* Counts:

  * total words
  * unique words
* Saves cleaned text to a file
* Generates a formatted analysis report

---

## 📂 Project Structure

```text
AI-with-Python
└── day-15
    ├── README.md
    ├── text_cleaner_cli.py
    ├── sample_input.txt
    ├── cleaned_text.txt
    └── analysis_report.txt
```

---

## ⚙️ How It Works

### Step 1: Input

User provides the file path:

```
Enter the file path: sample_input.txt
```

---

### Step 2: Processing

The program:

* reads file content
* converts text to lowercase
* removes punctuation using `string.punctuation`
* splits text into words

---

### Step 3: Analysis

* Total word count is calculated
* Unique words are extracted using `set()`

---

### Step 4: Output Files

### 📄 cleaned_text.txt

Contains processed text:

```
ai is the future python is powerful ai will transform industries
```

---

### 📄 analysis_report.txt

```
--- FILE ANALYSIS REPORT ---
Total Words: 11
Unique Words: 9
----------------------------
```

---

## 📊 Skills Demonstrated

* File handling (`with open`)
* Exception handling (`try / except`)
* String manipulation and cleaning
* Use of Python modules (`string`)
* Word tokenization
* Data analysis basics
* CLI-based program design

---

## 🧠 Relevance to AI

This project represents the **first stage of an AI pipeline**:

```
Raw Text → Cleaning → Tokenization → Analysis
```

These steps are essential in:

* Natural Language Processing (NLP)
* Retrieval-Augmented Generation (RAG)
* Chatbots and text-based AI systems
* Dataset preprocessing

---

## ⚠️ Error Handling

The program safely handles:

* missing files (`FileNotFoundError`)
* unexpected runtime errors

This ensures the program does not crash during execution.

---

## 🎯 Learning Outcome

By completing this project, you can:

* Build a complete file-based processing tool
* Clean and analyze real-world text data
* Understand how preprocessing works in AI systems
* Combine multiple Python concepts into one application

---

## 🚀 Future Improvements

* Remove extra spaces more efficiently
* Use faster text cleaning methods (`translate()`)
* Add support for multiple files
* Add stopword removal (NLP enhancement)
* Convert into a GUI or web app

---

## ▶️ How to Run

```bash
python text_cleaner_cli.py
```

Then enter the file path when prompted.

---
