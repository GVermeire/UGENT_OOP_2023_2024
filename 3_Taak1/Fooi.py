# invoer
Totaal_bedrag = float(input())
Percentage_fooi = float(input())

# Bewerking
Maal = (Percentage_fooi/100) + 1
oplossing = Totaal_bedrag*Maal

echte_oplossing = oplossing*100
v1 = int(echte_oplossing)
v2 = v1/100

# Uitvoer
print("Total amount including tip: €" + str(v2))
