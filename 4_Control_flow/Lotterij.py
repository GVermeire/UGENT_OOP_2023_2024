import random

# Seed instellen
random.seed(1) # # to make the random generator deterministic

# Variabele maken (lotterij)
Input = int(input("Voer een getal in tussen 0 en 99: "))
variabele = random.randint(0, 99) # random generator that generates a number between 0 and 99

print("The lottery number is", variabele)

# berekening
if variabele == Input:
    print("Exact match: you win 10.000 €")
elif sorted(str(Input)) == sorted(str(variabele)):
    print("Match all digits: you win 3.000 €")
elif str(Input)[0] == str(variabele)[0] or str(Input)[1] == str(variabele)[1] or str(Input)[0] == str(variabele)[1] or str(Input)[1] == str(variabele)[0]: # hier moest ik nog een string maken van die input en variabele zodak ze ook kon sorteren
    print("Matùch one digit: you win 1,000 €")
else:
    print("Sorry, no match")


