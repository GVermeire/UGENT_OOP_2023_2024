# invoer
a=int(input())
aantal_delers=0

for i in range(1,a+1):
    if a%i==0:
        aantal_delers+=1 # verhogen van object 'aantal_delers3 als je natuurlijk getal deelbaar was door één i
if aantal_delers==2: # nu testen of het getal 2 keer deelbaar is geweest zo ja -> priemgetal
    print('{} is een priemgetal'.format(a))
else:
    print('{} is geen priemgetal'.format(a))