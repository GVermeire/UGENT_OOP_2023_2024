# Gegeven gegevens
mijlen = 10
minuten = 92
kilometer_per_mijl = 1.6

# Omrekeningen
kilometers = mijlen * kilometer_per_mijl
uren = minuten / 60

# Bereken de snelheid in kilometers per uur
snelheid_kmh = kilometers / uren

# Geef het resultaat weer
print("De loper loopt gemiddeld", snelheid_kmh, "kilometer per uur.")
