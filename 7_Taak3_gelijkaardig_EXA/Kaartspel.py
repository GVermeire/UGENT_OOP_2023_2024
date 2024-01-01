import random

def kaartspel(seed):
    kleuren = ['Spades','Hearts','Diamonds','Clubs']
    kaartnummers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King',]

    deck = [(kaartnummer,kleur) for kleur in kleuren for kaartnummer in kaartnummers]
    deck_copy=deck.copy()
    random.seed(seed)

    random.shuffle(deck)
    gekozen_kaarten = deck[:4]


    for i, (kaartnummer, kleur) in enumerate(gekozen_kaarten, start=1):
        positie_in_deck = deck_copy.index((kaartnummer, kleur))
        print(f"Card number {positie_in_deck} is {kaartnummer} of {kleur}")

kaartspel(seed=1)