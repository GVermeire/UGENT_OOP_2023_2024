# invoer
rentepercentage = float(input("rente: "))
numberOfYears = int(input("jaren: "))
loanAmount = float(input("bedrag: "))

# Berekeningen
monthlyInterestRate = rentepercentage/12
monthlyPayment = loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (numberOfYears * 12)))
total_payment = monthlyPayment * 12 * numberOfYears

# Uitvoer
print("The monthly payment is", monthlyPayment)
print("The total payment is", total_payment)

## juiste oplossing van seppe
per=float(input())/100
jaren=int(input())
bedrag=float(input())
per_M=per/12
bedrag_M=(bedrag*per_M)/(1-(1/(1+per_M)**(jaren*12)))
totaal=bedrag_M*12*jaren
print("The monthly payment is {}".format(int(bedrag_M)))
print("The total payment is {}".format(int(totaal)))