print("#1")

def maximum(a,b):
    if a>b:
        return a
    elif a == b:
        return "Equal"
    else:
        return b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
answer = maximum(num1 , num2)

print(answer)
