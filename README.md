# Student Grade Manager

A simple, menu-driven Python application to manage student marks, calculate grades automatically, and display student performance summaries.

This project demonstrates fundamental Python programming concepts, including functions, loops, conditional statements, lists, dictionaries, input validation, and exception handling.

## Features

- **Add Student Records:** Enter student names and marks.
- **Automatic Grade Calculation:** Assign grades based on marks.
- **Input Validation:** Prevent empty names, invalid marks, and non-numeric inputs.
- **Duplicate Prevention:** Avoid adding the same student more than once.
- **Display Results:** View all student names, marks, and grades in a formatted table.
- **Class Average:** Automatically calculate the average marks of all students.
- **Top Performer:** Identify the student with the highest marks.
- **Interactive Menu:** Navigate through the application using a simple command-line menu.

## Grading System

| Marks Range | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

## Project Structure

```text
Student-Grade-Manager/
│
├── Student Grade Manager.py   # Main Python application
├── requirements.txt           # Project dependencies
├── .gitignore                 # Git ignored files
├── .gitattributes              # Git configuration
└── README.md                   # Project documentation
```

## Requirements

- Python 3.8 or above
- Visual Studio Code or any Python-compatible IDE
- Command Prompt or Terminal

**Dependencies:** No external Python packages are required. The application uses Python's built-in features.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sarvarajinfotech-code/Student-Grade-Manager.git
```

### 2. Navigate to the Project Directory

```bash
cd Student-Grade-Manager
```

### 3. Run the Application

```bash
python "Student Grade Manager.py"
```

If your system uses the Python launcher on Windows, you can also run:

```bash
py "Student Grade Manager.py"
```

## How to Use

Once the application starts, you will see the following menu:

```text
===== STUDENT MARKS MANAGEMENT =====

1. Add Student
2. Display Results
3. Exit

Choose an option (1-3):
```

### Option 1: Add Student

- Select `1` to add a student.
- Enter the student's name.
- Enter marks between 0 and 100.
- The application automatically calculates the corresponding grade.
- Duplicate student names are rejected.

### Option 2: Display Results

- Select `2` to view all student records.
- View individual marks and grades.
- Check the total number of students.
- View the class average.
- Identify the top-performing student.

### Option 3: Exit

- Select `3` to close the application.

## Example Output

```text
=======================================================
                   STUDENT RESULTS
=======================================================
Name                     Marks          Grade
-------------------------------------------------------
Arun                     95.00          A+
Priya                    82.00          A
Karthik                  74.00          B
Divya                    65.00          C
-------------------------------------------------------
Total Students: 4
Class Average: 79.00
Top Student: Arun (95.00)
=======================================================
```

*Note: This is an illustrative example of the expected output.*

## Python Concepts Practiced

This project provides practical experience with:

- Variables and data types
- Functions and modular programming
- Lists and dictionaries
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while` and `for`)
- User input and output
- Exception handling (`try` and `except`)
- Data validation
- List operations and built-in functions
- Code readability and organization

## Current Limitations

- Student records are stored in memory and are not permanently saved.
- All records are cleared when the application exits.
- The application currently supports command-line interaction only.

## Future Enhancements

- Save student records using CSV or JSON files.
- Add options to update and delete student records.
- Search for students by name.
- Generate individual student report cards.
- Introduce a graphical user interface.
- Add persistent database storage.

## Learning Outcome

The Student Grade Manager project was developed as a hands-on Python learning exercise to understand how basic programming concepts can be combined to build a functional application.

It focuses on writing structured, reusable code while handling real-world scenarios such as invalid inputs, duplicate records, and student performance calculations.

---

**Developed as part of a Python Programming Learning Assignment.**

