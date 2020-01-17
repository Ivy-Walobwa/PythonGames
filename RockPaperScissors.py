import random

def rock_paper_scissors_game():
    weapons = ['r', 'p', 's']
    random_number = random.randint(0, 2)
    comp_weapon = weapons[random_number]

    user_weapon = input('Rock(r), Paper(p) or Scissors(s)? ').lower()
    print(f'You picked {user_weapon}')
    print(f'Computer picks {comp_weapon}')

    if user_weapon == comp_weapon:
        print(f'{user_weapon} and {comp_weapon}, you tie!')
    elif (user_weapon == 'r' and comp_weapon == 'p') or (user_weapon == 's' and comp_weapon == 'r') or (user_weapon == 'p' and comp_weapon == 's'):
        print('You lose!')
    elif (user_weapon == 'r' and comp_weapon == 's') or (user_weapon == 'p' and comp_weapon == 'r') or (user_weapon == 's' and comp_weapon == 'p'):
        print('You win!')
    else:
        print('Pick valid weapon')


name = input('What is your name? ')
print(f'Hello {name}, welcome to rock paper scissors. ')
start_game = input('Would you like to start? Y/N ').lower()

if start_game == 'n':
    print('Okay, bye!')
else:
    rock_paper_scissors_game()