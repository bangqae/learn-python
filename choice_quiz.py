# Multiple Choice Quiz, Learn Python - Full Course for Beginners [Tutorial]
from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),  # Using the Question class to insert question_prompts and answer
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):  # Pass the questions array that contain question and answer
    score = 0
    print("There're " + str(len(questions)) + " quiz")  # len : array length
    for i in questions:  # Start of the for loop
        answers = input(i.prompt)  # Variable to contain the answer, with prompt as the output (see the Question class)
        if answers == i.answer:  # Compare answers variable to answer from questions array
            score += 1  # End of the loop
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
