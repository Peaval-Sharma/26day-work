# Python CLI Quiz Application 🐍

A simple **Command-Line Interface (CLI) Quiz Application** built using Python.
The program asks multiple-choice questions about Python programming and calculates the final score and percentage.

## 📌 Features

* 10 Python-related multiple-choice questions
* Questions are shuffled randomly
* Accepts answers in **A, B, C, or D** format
* Handles invalid answers
* Shows whether the answer is correct or wrong
* Displays the correct answer for incorrect responses
* Calculates:

  * Total questions
  * Correct answers
  * Wrong answers
  * Score
  * Percentage
* Displays a performance message based on the percentage

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Command Line / Terminal

## 📂 Project Structure

```text
Python-CLI-Quiz/
│
├── quiz.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check Python version:

```bash
python --version
```

### 2. Run the Program

Open the project folder in VS Code or Terminal and run:

```bash
python quiz.py
```

## 🎮 How to Play

1. The program displays a Python question.
2. Four options are shown: **A, B, C, and D**.
3. Enter your answer.
4. If the answer is correct, the program displays:

```text
Correct! ✓
```

5. If the answer is incorrect, it displays:

```text
Wrong! ✗
Correct answer: B
```

6. After all 10 questions, the final result is displayed.

## 📊 Result System

The application evaluates the percentage using the following conditions:

| Percentage   | Result                 |
| ------------ | ---------------------- |
| 80% or above | Excellent! 🎉          |
| 60% – 79%    | Good Job! 👍           |
| 40% – 59%    | Keep Practicing! 📚    |
| Below 40%    | Need More Practice! 💪 |

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* Lists
* Dictionaries
* `random.shuffle()`
* `for` loops
* `while` loops
* `if-elif-else`
* `input()`
* String methods such as `.upper()`
* `enumerate()`
* F-strings
* Arithmetic calculations
* User input validation
* Dictionary access
* Basic error handling through input validation

## 🔀 Random Question Order

The program uses:

```python
random.shuffle(questions)
```

This randomly changes the order of the questions every time the quiz starts.

## 📈 Example Output

```text
==================================================
          PYTHON CLI QUIZ APPLICATION
==================================================

There are 10 questions.
Enter A, B, C or D as your answer.

Question 1: Which keyword is used to define a function in Python?

A. function
B. define
C. def
D. fun

Your answer: C
Correct! ✓

==================================================
              QUIZ RESULT
==================================================

Total Questions : 10
Correct Answers : 8
Wrong Answers   : 2
Score           : 8/10
Percentage      : 80.00%
Result: Excellent! 🎉
==================================================
Thank you for playing!
```

## 🎯 Learning Objective

The main objective of this project is to practice Python programming concepts by creating an interactive quiz application using **lists, dictionaries, loops, conditions, functions from modules, input validation, and basic calculations**.

## 🚀 Future Improvements

The project can be improved by adding:

* More quiz questions
* Different quiz categories
* Difficulty levels
* Timer for each question
* High-score system
* Multiple quiz attempts
* Player name
* Saving scores to a file
* GUI version using Tkinter
* Web version using HTML, CSS, and Flask

## 👨‍💻 Author

**Python CLI Quiz Application by praval**

Made using Python 🐍
