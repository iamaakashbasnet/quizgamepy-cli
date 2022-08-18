"""
Quiz game

Format:
    questions = {
        "question": "correct option here..."
    }

    options = [
        [options for first questions],
        [options for second questions]
    ]
"""


def main():

    questions = {
        "Who created Python?: ": "A",
        "What year was Python created?: ": "B",
        "Python is tributed to which comedy group?: ": "C",
        "Is the Earth round?: ": "A"
    }

    options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
               ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
               ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
               ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

    def new_game():
        guesses = []
        correct_guesses = 0
        question_num = 1

        for key in questions:
            print('---------------------------------')
            print(key)
            for i in options[question_num - 1]:
                print(i)

            guess = input('Enter (A,B,C or D): ').upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)

            question_num += 1

        display_score(correct_guesses, guesses)

    def check_answer(answer, guess):
        if answer == guess:
            print('Correct!')
            return 1
        else:
            print('Wrong!')
            return 0

    def display_score(correct_guesses, guesses):
        print('-------------------------')
        print('RESULTS')
        print('-------------------------')

        print('Answers:', end='')
        for i in questions:
            print(questions.get(i), end=' ')
        print()

        print('Guesses:', end='')
        for i in guesses:
            print(i, end=' ')
        print()

        score = int((correct_guesses/len(questions))*100)
        print(f'Your score is {score}%')

    def play_again():
        response = input('Do you want to play again? (y/n): ').upper()

        if response == 'Y':
            return True
        else:
            return False

    new_game()

    while play_again():
        new_game()


if __name__ == '__main__':
    main()
