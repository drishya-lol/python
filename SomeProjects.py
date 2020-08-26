#1

print("#1")
radius = int(input("The radius of the circle you want: "))
pi = 3.14
area = pi * radius ** 2

print("The area of the circle with" , radius , "is" , area)

#2

print("")
print("#2")
intry = int(input("Enter the number whose multiplication table you want: "))
maxVal = int(input("Enter the maximum limit: "))
i=1

while i <= maxVal:
    answers =  intry * i
    print(str(intry) , "*" , i , "=" , answers)
    i += 1

#3

print("")
print("#3")
number = int(input("Enter the \"Integer\" you want to check for odd or even: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#4

print("")
print("#4")

celTemp = float(input("Celsius Temperature you want to convert in Fahrenheit: "))

fahTemp = (9 / 5) * celTemp + 32

print("The temperature in Fahrenheit scale is" , fahTemp)

#5

print("")
print("#5")

names = ["drishya", "kisne" , "ganesh"]
print(names)
i = 0

while i<=2:
    for first in names:
        print(first[0]+str(len(names[i])))
        i += 1

#6

print("")
print("#6")

dict1 = {"name" : "Drishya", "age" : 19, "location" : "kaushaltar"}
dict2 = {"name" : "Pankaj", "age" : 17, "location" : "harsachowk"}
dict3 = {"name" : "Asim", "age" : 19, "location" : "katunje"}

print(dict1 , type(dict1))
print(dict2 , type(dict2))
print(dict3 , type(dict3))

dicts = dict1 , dict2 , dict3
required = list(dicts)

print(required, type(required))

#7

print("")
print("#7")

curYear = int(input("Enter the current year: "))
birthYear = int(input("Enter  the year you were born: "))

age = curYear - birthYear

print("Your age is" , age)

#8

print("")
print("#8")

print("The even numbers from 1 and 100 are: ")
for i in range(2, 101, 2):
    print(i)

#9

print("")
print("#9")

listed = ['d','r','i','s','h','y','a']
print(listed, type(listed))

joined = "".join(listed)
print(joined, type(joined))

#10

print("")
print("#10")

number = int(input("Enter any number: "))

if number % 5 == 0:
    print(number)
else:
    print("no")















