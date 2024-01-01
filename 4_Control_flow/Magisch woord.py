# Vraag de gebruiker om de zin in te voeren
print("Geef de zin die het toverwoord bevat.\n")
zin = input("")

# Zoek naar de positie van het toverwoord tussen aanhalingstekens
begin_index = zin.find('"') + 1 # zoeken naar eerste positie van "
eind_index = zin.rfind('"') #reverse find doen om de laatste " te vinden

# Haal de naam en het toverwoord uit de zin
naam = zin[12:begin_index - 24]
toverwoord = zin[begin_index:eind_index]

# Toon de gevonden informatie
print(f"Het toverwoord van {naam} is \"{toverwoord}\". De lengte van het toverwoord is {len(toverwoord)} letters.")
