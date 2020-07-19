def check(speed):
    if speed <= 70:
        return "OK"
    else:
        demerit = (speed - 70)/5
        if demerit <= 12:
            return "Demerit points: " + str(demerit)
        else:
            return "License suspended"
        
entry = int(input("His speed: "))
print(check(entry))
        
