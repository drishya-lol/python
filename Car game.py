command = ''
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
            if started:
                print('\nCar already started!')
            else:
                started = True
                print('\nCar is started! ')
    elif command == 'stop':
            if not started:
                print('\nCar already stopped! ')
            else:
                started = False
                print('\nCar is stopped! ')
    elif command == 'help':
        print(f'\nstart > starts the car\nstop > stops the car\nquit > ends the program\n')
    elif command == 'quit':
        print('\nBye bye\n')
        break
    else:
        print("\nI did not understand that! please type 'help' for help!\n")