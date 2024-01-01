# Invoer
massa_in_kg = int(input("nummer voor massa: "))
lichaamslengte_in_cm = int(input("nummer voor lichaamslengte in cm: "))
leeftijd_in_jaren = int(input("nummer voor leeftijd in jaren: "))

# gegeven
chocoladereep_in_calorieen = 230

# BMR berekenen
BMR_man = 66.4730 + (13.7516 * massa_in_kg) + (5.0033 * lichaamslengte_in_cm) - (6.7550 * leeftijd_in_jaren)
BMR_vrouw = 655.0955 + (9.5634 * massa_in_kg) + (1.8496 * lichaamslengte_in_cm) - (4.6756 * leeftijd_in_jaren)

# Omrekeningen
Oplossing_man = BMR_man/chocoladereep_in_calorieen
Oplossing_vrouw = BMR_vrouw/chocoladereep_in_calorieen

# geef het resultaat weer
print("Een man moet dagelijks", Oplossing_man, "chocoladerepen eten om zijn gewicht te behouden. Een vrouw moet dagelijks", Oplossing_vrouw, "chocoladerepen eten om haar gewicht te behouden.")
