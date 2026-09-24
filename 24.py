import random

# Quiz Questions
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .java", "B. .py", "C. .html", "D. .cpp"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store multiple values in a list?",
        "options": ["A. list", "B. int", "C. float", "D. bool"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    },
    {
        "question": "Which function is used to take input from the user?",
        "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used for a loop over a sequence?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. string", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "What is the output of 2 + 3 * 2?",
        "options": ["A. 10", "B. 8", "C. 12", "D. 7"],
        "answer": "B"
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": ["A. lower()", "B. small()", "C. lowercase()", "D. down()"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a class?",
        "options": ["A. object", "B. class", "C. create", "D. structure"],
        "answer": "B"
    }
]


# Shuffle questions
random.shuffle(questions)

score = 0

print("=" * 50)
print("          PYTHON CLI QUIZ APPLICATION")
print("=" * 50)

print("\nThere are 10 questions.")
print("Enter A, B, C or D as your answer.\n")


# Quiz loop
for number, question in enumerate(questions, start=1):

    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    # Handle invalid answers
    while True:
        user_answer = input("Your answer: ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid answer! Please enter A, B, C or D.")

    # Check answer
    if user_answer == question["answer"]:
        print("Correct! ✓")
        score += 1
    else:
        print("Wrong! ✗")
        print(f"Correct answer: {question['answer']}")


# Final Result
total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n" + "=" * 50)
print("              QUIZ RESULT")
print("=" * 50)

print(f"Total Questions : {total_questions}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {total_questions - score}")
print(f"Score           : {score}/{total_questions}")
print(f"Percentage      : {percentage:.2f}%")

if percentage >= 80:
    print("Result: Excellent! 🎉")
elif percentage >= 60:
    print("Result: Good Job! 👍")
elif percentage >= 40:
    print("Result: Keep Practicing! 📚")
else:
    print("Result: Need More Practice! 💪")

print("=" * 50)
print("Thank you for playing!")