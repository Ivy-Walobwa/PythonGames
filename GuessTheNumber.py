import random

def play_game(guess_limit, secret_number, guess_count):
    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1
        if guess > secret_number:
            print('Number too high!')
        elif guess < secret_number:
            print('Number too low')
        elif guess == secret_number:
            print(f'You won in {guess_count} guesses! ')
            break
    else:
        print('You lose!')


def guessing_game():
    game_instructions = '''
    I am thinking of a number between 1 and 20. 
    Take a guess!
    Remember you have three chances.
    '''
    guess_limit = 3
    guess_count = 0
    secret_number = random.randint(1, 21)

    if start_game == 'n':
        print('Okay, bye')
    else:
        print(game_instructions)
        play_game(guess_limit, secret_number, guess_count)


name = input('Hello! What is your name? ')
print(f'Hello {name}, welcome to Guess the Number. ')
start_game = input('Would you like to proceed? Y/N ').lower()
guessing_game()