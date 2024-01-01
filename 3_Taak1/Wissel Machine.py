# Start
print("Ik vind voor jou de combinatie aan centjes dat overeenkomt met een bepaald bedrag.")

# invoer
centjes = int(input("Geef een bedrag tussen 0 en 100: "))

print(str(centjes), "centje(s) bestaat uit:")

# Functie definieren met parameter 'centjes'
def wisselmachine(centjes):
    munten = [50, 20, 10, 5, 2] # i variabelen in deze
    resultaat = {} # i variabelen

    for i in range(5):      #zal een iteratie uitvoeren voor elke variabele in de lijst 'munten'
        resultaat[i] = centjes // munten[i]
        centjes = centjes % munten[i]
        print(str(resultaat[i]), "centje(s) van", str(munten[i]), "cent") # geindenteert zodat hij dit i keer herhaalt
    print(str(centjes), "centje(s)") # deze niet geindenteerd aangezien we niet willen dat hij dit 5 keer zou herhalen

wisselmachine(centjes)



