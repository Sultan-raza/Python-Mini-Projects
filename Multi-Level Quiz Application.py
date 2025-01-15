# Easy level questions
easy_questions = [
    ("What is the capital of France?", ["1. Berlin", "2. London", "3. Paris", "4. Madrid"], 3),
    ("What is 2 + 2?", ["1. 3", "2. 4", "3. 5", "4. 6"], 2),
    ("What is the color of the sky?", ["1. Green", "2. Red", "3. Blue", "4. Yellow"], 3)
]

# Medium level questions
medium_questions = [
    ("What is the largest planet in our solar system?", ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"], 3),
    ("Who wrote 'To Kill a Mockingbird'?", ["1. Harper Lee", "2. Mark Twain", "3. Ernest Hemingway", "4. F. Scott Fitzgerald"], 1),
    ("What is the square root of 64?", ["1. 6", "2. 7", "3. 8", "4. 9"], 3)
]

# Hard level questions
hard_questions = [
    ("What is the chemical symbol for gold?", ["1. Ag", "2. Au", "3. Pb", "4. Fe"], 2),
    ("In which year did World War I begin?", ["1. 1912", "2. 1914", "3. 1916", "4. 1918"], 2),
    ("What is the capital of Iceland?", ["1. Oslo", "2. Reykjavik", "3. Stockholm", "4. Helsinki"], 2)
]

# Function to conduct the quiz
def quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        print("\n" + question)
        for option in options:
            print(option)
        while True:
            try:
                answer = int(input("Your answer (1-4): "))
                if 1 <= answer <= 4:
                    if answer == correct_answer:
                        print("Correct!")
                        score += 1
                    else:
                        print("Incorrect.")
                    break
                else:
                    print("Invalid input, please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input, please enter a number.")
    return score

# Main function to execute the quiz application
def main():
    print("Welcome to the Multi-Level Quiz Application!")
    
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level = ''
    while True:
        try:
            difficulty = int(input("Your choice (1-3): "))
            if difficulty == 1:
                selected_questions = easy_questions
                level = 'Easy'
                break
            elif difficulty == 2:
                selected_questions = medium_questions
                level = 'Medium'
                break
            elif difficulty == 3:
                selected_questions = hard_questions
                level = 'Hard'
                break
            else:
                print("Invalid input, please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input, please enter a number.")
    print(f"You selected {level} level. Let's start the quiz!")
    total_score = quiz(selected_questions)
    print(f"\nQuiz Completed. Your total score is: {total_score}/{len(selected_questions)}")

if __name__ == "__main__":
    main()
