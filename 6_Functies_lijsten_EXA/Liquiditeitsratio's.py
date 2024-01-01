def calculate_current_ratio(activa, vorderingen, schulden, passiva):
    currentratio = (activa-vorderingen)/(schulden + passiva)
    return f"De current ratio van de onderneming bedraagt: {round(currentratio, 2)}"

def calculate_acid_test_ratio(activa, vorderingen_meer_dan_1_jaar, schulden_op_1_jaar, voorraden_en_bestellingen):
    acid_test_ratio = (activa - vorderingen_meer_dan_1_jaar - voorraden_en_bestellingen) / schulden_op_1_jaar
    return f"De acid test ratio van de onderneming bedraagt: {round(acid_test_ratio, 2)}"

