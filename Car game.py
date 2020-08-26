command = ''
started = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started.')
        else:
            started = True
            print('Car started! ')
    elif command == 'stop':
        if not started:
            print('Car is already stopped.')
        else:
            started = False
            print('Car stopped! ')
    elif command == 'help':
        print(f' start > start the car\nstop >  stop the car\nquit >  end the program')
    elif command == 'quit':
        break
    else:
        print("I don't understand that.")