Merk = str(input("Geef me een merk:"))
Plaats = str(input("geef me een plaats"))
merk = Merk.casefold()
plaats = Plaats.casefold()
i = 0
h = 0

while i < len(plaats) and h < len(merk):
    if merk[h] == plaats[i]:
        j = 0
        while i + j < len(plaats) and h + j < len(merk) and merk[h + j] == plaats[i + j]:
            j += 1

        if j > 0:
            print(f'[{Merk[h:h+j]}]', end="")
            i += j
            h += j
        else:
            print(f'{Merk[h]}', end="")
            h += 1
    else:
        print(f'{Merk[h]}', end="")
        h += 1

print(Merk[h:])
