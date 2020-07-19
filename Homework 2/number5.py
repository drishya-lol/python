def max(a, b ,c):
    if a>b and a>c:
        return "a is max"
    elif b>a and b>c:
        return "b is max"
    else:
        return "c is max"


num1 = int(input("Enter a number: "))
num2 = int(input("Enter b number: "))
num3 = int(input("Enter c number: "))

print(max(num1 , num2 , num3))
