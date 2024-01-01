# zet je oplossing in de functie main
def main():
    gewicht=float(input(""))

    lengte=int(input(""))
    lengte=lengte/100
    bmi = (gewicht) / (lengte *lengte)
    gezondheid=""
    if bmi < 18.5:
        gezondheid="Ondergewicht"
    elif bmi < 25:
        gezondheid="Gezond gewicht"
    elif bmi < 30:
        gezondheid="Overgewicht"
    else:
        gezondheid="Obesitas"
    print(f"{bmi:.2f}")
    print(gezondheid)



