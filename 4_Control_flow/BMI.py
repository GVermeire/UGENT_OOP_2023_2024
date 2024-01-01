gewicht = float(input())
lengte = float(input())

# berkening
BMI = gewicht / lengte**2

# uitvoer
if BMI < 18:
    print(BMI)
    print("Ondergewicht")
else:
    if BMI <25:
        print(BMI)
        print("Normaal gewicht")
    else:
        if BMI < 30:
            print(BMI)
            print("Overgewicht")
        else:
            if BMI > 30:
                print(BMI)
                print("Obesitas")