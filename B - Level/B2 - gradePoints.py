points = int(input("Gib die PunkteZahl ein: "))

if points < 0 or points > 100:
    print("Diese Punktzahl stimmt nicht!")
else:
    if points > 90:
        print("Sehr gut!")
    elif points > 60:
        print("Bestanden!")
    elif points > 30:
        print("Nachpruefung!")
    else:
        print("Nicht Bestanden ):")