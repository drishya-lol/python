intry = int(input("Enter the number whose multiplication table you want: "))
maxVal = int(input("Enter the maximum limit: "))
i=1

while i <= maxVal:
    answers =  intry * i
    print(str(intry) , "*" , i , "=" , answers)
    i += 1
