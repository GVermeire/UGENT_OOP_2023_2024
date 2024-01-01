# Invoer van tien natuurlijke getallen
getallen = [int(input()) for _ in range(10)]

# Bepaal het grootste en het kleinste getal
max_getal = max(getallen)
min_getal = min(getallen)

# Bepaal het aantal drievouden
aantal_drievouden = sum(1 for getal in getallen if getal % 3 == 0)

# Uitvoer
print("grootste: {}".format(max_getal))
print("kleinste: {}".format(min_getal))
print("drievouden: {}".format(aantal_drievouden))