weight = float(input('Weight: '))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    weight = weight / 2.2
    print(f'You are {int(weight)} kg.')
elif unit.upper() == 'K':
    weight = weight * 2.2
    print(f'You are {int(weight)} pounds.')