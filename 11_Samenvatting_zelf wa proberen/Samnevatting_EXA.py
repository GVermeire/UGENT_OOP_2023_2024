print("\"hello\"")
#print(""hello"") dit werkt nie
print("\ntekst") #dit zal voor het afprinten van "tekst" een lijn overslaan

def __init__(self, name:str): #dit toont hoe je kan zeggen welke soort van invoer name moet zijn
def add_player(self, player: SoccerPlayer) -> bool:


print("AAA", end = ' ')
print("BBB", end = '')
print("CCC", end = '***')
print("DDD", end = '***') # de reden dat na dit "ik ben gianni" ook wordt afgeprint naast alles is omdat j ehier heb bepaald dat 'end' geen \n inhoudt. Terwijlk een normale print wel naar de volgende lijn gaat doet die da thier dus niet
#Deze print hierboven heeft dfus een impact op de weergave van de volgende print omdat de print hierboven geen nieuwe lijn initialiseert
A = "ik ben gianni"
stripped = A.strip() # de stript functie gaat andere vormen van "end" verwijderen dus als je zoals hier eerst end = '   ' gedaan hebt gaat stripped zorgen data vanaf nu normaal velroopt
print(stripped)
print("test of dit nog steeds na \"ik ben gianni\" wordt weergegeven") # ANTWOORD IS NEEN want na ik ben gianni heb je geen speciale end toegvoegd
print(format(59832, '<10d')) # print gwn de waarde af aangezien je vraagt om het decimaal te doen
print(format(59832, '10b')) # print de input maar dan als binaire waarde
print(format(1110100110111000, '10d')) # dit zal een decimaal getal niet omzetten naar een binair getal aangezien pyhton denkt dat de input al een decimaal getal is
# om van binair naar decimaal te gaan gebruik je best volgende:
print(int(str(1110100110111000), 2))

# we kunnen de format dingen dus ook zo toevoegen rechtstreeks in een f string das veel handiger dan telkens die format functie te schrijven
Test = 1999
print(f"Dit is een test {Test:>10d}")

count = 0
while count < 100:
    print("Programming is fun!")
    count += 1