# Invoer
Startkapitaal = float(input("Startkapitaal: "))
Rentevoet = float(input("Rente: "))
Aantaljaar = int(input("Jaren: "))

v1 = Startkapitaal # tussenwaarde berekenen voor de winst te berekenen

# berekeningen
for i in range(Aantaljaar):
    bedrag1 = Startkapitaal * (1 + Rentevoet)
    print(f'Bedrag na {i + 1} jaar: €{bedrag1:.2f}.')
    Startkapitaal = bedrag1
    winst_of_verlies = bedrag1 - v1
    if i == Aantaljaar-1 and winst_of_verlies < 0:
        print(f"Na {Aantaljaar} jaar bedraagt het verlies €{-winst_of_verlies:.2f}.")
    elif i == Aantaljaar-1 and winst_of_verlies > 0:
        print(f"Na {Aantaljaar} jaar bedraagt de winst €{winst_of_verlies:.2f}.")