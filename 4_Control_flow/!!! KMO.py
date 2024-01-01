x=''
a=0
b=0
c=0
d=0
while x!='nee':
    werknemers = int(input())
    omzet = float(input())
    balans = float(input())
    percentage = int(input())
    if werknemers < 250:
        a = 1
    if omzet < 50000:
        b = 1
    if balans < 43000:
        c = 1
    if percentage < 25:
        d = 1
    if a == 1 and b == 1 and d == 1 or a== 1 and c == 1 and d == 1:
        print("Het bedrijf is EEN KMO")
    else:
        print("Het bedrijf is GEEN KMO")
    # Hier reset je je a, je b, je c en je d, zodat je de code opnieuw zou kunnen uitvoeren.
    a = 0
    b = 0
    c = 0
    d = 0
    antw = input()
    x = antw.lower()