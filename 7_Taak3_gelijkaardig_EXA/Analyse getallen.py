def analyze_numbers(l):
    gemiddelde = sum(l) / len(l)
    k=0
    for i in l:
        if i>gemiddelde:
            k+=1
    print(f"Average is {gemiddelde}")
    print(f"Number of elements above the average is {k}")