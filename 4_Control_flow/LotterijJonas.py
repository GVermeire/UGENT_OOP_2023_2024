import random

random.seed(1)
loting = random.randint(0, 99)
loting_tiental = loting // 10
loting_eenheid = loting % 10

getal = int(input())
getal_tiental = getal // 10
getal_eenheid = getal % 10

if loting == getal:
    print(f"The lottery number is {loting}")
    print("Exact match: you win 10.000 €")
elif getal_tiental == loting_eenheid and getal_eenheid == loting_tiental:
    print(f"The lottery number is {loting}")
    print("Match all digits: you win 3,000 €")
elif getal_tiental == loting_eenheid or getal_eenheid == loting_tiental or getal_tiental == loting_tiental or getal_eenheid == loting_eenheid:
    print(f"The lottery number is {loting}")
    print("Match one digit: you win 1,000 €")
else:
    print(f"The lottery number is {loting}")
    print("Sorry, no match")
