import random

a = random.randint(1,6)    
guess = 0

while guess != a:
    guess = int(input('Enter a number between 1 and 6: '))
    if guess < a:
        print('Guess a little higher.')
    elif guess > a:
        print('Guess a little lower.')
    else:
        print('You guessed it right.')