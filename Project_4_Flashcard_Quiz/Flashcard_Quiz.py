import random

# Define the question dictionary
question_dict = {
    1: {"question": "How many continents are in the world?", "options": [4, 9, 7], "answer": 7},
    2: {"question": "Which year did Nigeria gain independence?", "options": [2000, 1960, 1940], "answer": 1960},
    3: {"question": "Who is the greatest footballer in the world?", "options": ["Messi", "Neymar", "Ronaldo"], "answer": "Messi"},
    4: {"question": "What is the capital of Japan?", "options": ["Beijing", "Tokyo", "Seoul"], "answer": "Tokyo"},
    5: {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Pacific", "Indian"], "answer": "Pacific"},
    6: {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Jupiter", "Venus"], "answer": "Mars"},
    7: {"question": "How many states are in Nigeria?", "options": [36, 30, 27], "answer": 36},
    8: {"question": "Which country hosted the 2014 FIFA World Cup?", "options": ["Germany", "Brazil", "South Africa"], "answer": "Brazil"},
    9: {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2"], "answer": "H2O"}
}


# question fucntion
def ask_question(score, questions_left):
    key = random.choice(questions_left)
    question_info = question_dict[key]
    
    print(f"\nQuestion: {question_info['question']}")
    for i, option in enumerate(question_info["options"], 1):
        print(f"{i}. {option}")

    answer_input = input("Enter the number of your answer: ")
    if answer_input.isdigit():
        answer_index = int(answer_input) - 1
        if 0 <= answer_index < len(question_info["options"]):
            user_answer = question_info["options"][answer_index]
            if user_answer == question_info["answer"]:
                score += 1
                print("Correct! Your score is now:", score)
            else:
                print("Wrong answer. The correct answer was:", question_info["answer"])
            questions_left.remove(key)
        else:
            print("Please enter a valid option number.")
    else:
        print("Invalid input. Please enter a number corresponding to the options.")

    return score

# Main loop
score = 0
questions_left = list(question_dict.keys())

while questions_left:
    score = ask_question(score, questions_left)
    if input("Do you want to answer another question? (yes/no): ").strip().lower() != 'yes':
        break

print("Thanks for playing! Your final score is:", score)
