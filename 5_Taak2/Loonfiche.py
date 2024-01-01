bruto_loon_WN = float(input())
rsz = bruto_loon_WN * 0.1307
belastbaar_inkomen = bruto_loon_WN - rsz
bedrijfs_voorheffing = belastbaar_inkomen * 0.30
nettoloon = belastbaar_inkomen - bedrijfs_voorheffing

print("brutoloon werknemer:")
print("==========================================")
print("|               LOONFICHE                |")
print("==========================================")

#brutoloon
print("|", end="") #Dit stuk code drukt een verticale lijn af (|) zonder een nieuwe regel te beginnen (end=""). Dit zorgt ervoor dat de uitvoer doorgaat op dezelfde regel.
print(format("Brutoloon",'<28s'), end= "") #Hier gebruiken we de ingebouwde Python-functie format() om de tekst "Brutoloon" in een kolom van 28 karakters links uit te lijnen ('<28s'). Dit betekent dat "Brutoloon" links wordt uitgelijnd in een kolom van 28 tekens breed. De resterende ruimte aan de rechterkant wordt gevuld met spaties.
print("|",end="")
print(format(bruto_loon_WN,'10.2f'), end= "")
print(" |")
print("|----------------------------------------|")

#rsz
print("|", end="")
print(format("RSZ bijdrage",'<28s'), end= "")
print("|",end="")
print(format(rsz*(-1),'10.2f'), end= "") # De min 1 staat er om het negatief te maken op de loonfiche.
print(" |")
print("|----------------------------------------|")

# Belastbaar inkomen
print("|", end="")
print(format("Belastbaar inkomen",'<28s'), end= "")
print("|",end="")
print(format(belastbaar_inkomen,'10.2f'), end= "")
print(" |")
print("|----------------------------------------|")

# Bedrijfsvoorheffing
print("|", end="")
print(format("Bedrijfsvoorheffing",'<28s'), end= "")
print("|",end="")
print(format(bedrijfs_voorheffing*(-1),'10.2f'), end= "") # De min 1 staat er om het negatief te maken op de loonfiche.
print(" |")
print("|----------------------------------------|")

# nettoloon
print("|", end="")
print(format("Nettoloon",'<28s'), end= "")
print("|",end="")
print(format(nettoloon,'10.2f'), end= "")
print(" |")
print("|----------------------------------------|")
