questions = [
    {
        "question": "Capital of India?",
        "answer": "Delhi"
    },
    {
        "question": "Python is a programming language? (yes/no)",
        "answer": "yes"
    },
    {
        "question": "2 + 2 = ?",
        "answer": "4"
    }
]

score = 0

for q in questions:
    ans = input(q["question"] + " ")

    if ans.lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your score is:", score, "/", len(questions))