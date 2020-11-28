import random


def guessing_game():
    answer = random.randint(0, 100)

    name = input('Enter your name: ')
    print(f'Hello, {name}!')

    guesses = 0

    while guesses < 3:
        guesses += 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
        if guesses == 3:
            print(f'You are out of guesses. The answer was {answer}')
            play_again = input('Enter y if you want to play again, or n to quit. ')
            if play_again == 'y':
                guessing_game()
            else:
                break


guessing_game()



