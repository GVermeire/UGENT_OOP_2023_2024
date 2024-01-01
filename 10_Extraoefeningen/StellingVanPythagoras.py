import math
# Invoer van de lengtes van de rechthoekszijden
a = float(input("Geef lengte rechthoekszijde: "))
b = float(input("Geef lengte rechthoekszijde: "))

# Berekening van de lengte van de schuine zijde
c = math.sqrt(a**2 + b**2)

# Uitvoer met afronding tot drie cijfers na de komma
print("Lengte van de schuine zijde: {:.3f}".format(c))