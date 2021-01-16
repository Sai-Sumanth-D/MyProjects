# first importing random from lib
import random as r

# to set a random number range
num = r.randrange(100)

# no of chances for the player to guess the number
guess_attempts = 5

# setting the conditions

while guess_attempts >= 0:
    player_guess = int(input('Enter your guess : '))

    # for checking the players guess = the actual number

    def check(x):
        if player_guess == x:
            print('You Won!!')
        elif player_guess > x:
            print('You are a bit on the higher side of the number, try lower!')
        else:
            print('Your guess is a bit on the lower side, try higher!')

    if guess_attempts > 1:
        check(num)
    elif guess_attempts == 1:
        check(num)
        print('This is your last chance, try making most of it.')
    else:
        print('You Lost')

    guess_attempts -= 1
