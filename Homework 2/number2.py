def fizz_buzz(entry):
    if entry % 3 == 0 and entry % 5 == 0:
        return "FizzBuzz"
    elif entry % 3 == 0:
        return "Fizz"
    elif entry % 5 == 0:
        return "Buzz"
    else:
        return str(entry)

number = int(input("Enter the number: "))

print(fizz_buzz(number))
