import random
guessCount = 0
guess_limit = 3
secretNumber = random.randint(1, 3)

while guessCount < guess_limit:
    guess = int(input('Guess: '))
    guessCount += 1
    if guess == secretNumber:
        print('You Won!')
        break
    else:
        print('Try again!')
else:
    print('Sorry, You\'ve failed')
