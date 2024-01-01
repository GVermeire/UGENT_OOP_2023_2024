# komt uit 5_OOP_loops
# checken op palindroom
def palindroom(str):
    index = 0
    index_omgekeerd = len(str) -1 #-1 aangezien length echt elk karakter telt en de index al start van 0
    if str[index] == str[index_omgekeerd]:
        index += 1
        index_omgekeerd -= 1
        print("dit is een palindroom")
    else:
        print(f"Dit is geen palindroom")

palindroom(str(input("Geef woord in: ")))

# je zou dit btr eens proberen met een while lus ipv met deze IF te werken
def palindroom(str):
    index = 0
    index_omgekeerd = len(str) -1 #-1 aangezien length echt elk karakter telt en de index al start van 0
    while str[index] == str[index_omgekeerd]:
        index += 1
        index_omgekeerd -= 1
    else:
        print(f"Dit is geen palindroom")

palindroom(str(input("Geef woord in: ")))
