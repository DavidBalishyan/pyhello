# Quiz game in python

questions = {
    "What is the capital of France?": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "What is the capital of Germany?": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "What is the capital of Italy?": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    }
}

score = 0

for question in questions.values():
    answer = input(question["question"] + " ")
    if answer.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Sorry, that's wrong. The correct answer is " + question["answer"])

print("Your final score is " + str(score) + "/" + str(len(questions)))
