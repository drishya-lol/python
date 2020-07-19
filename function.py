def add(*x):
    sums = 0
    for i in x:
        sums = sums + i
    return sums


def mul(*x):
    product = 1
    for i in x:
        product = product * i
    return product


print(mul(*range(1, 10)))
        

print(add(1, 2, 3, 4 , 55 ,102))
