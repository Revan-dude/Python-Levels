# Aufgabe: Schreibe eine Funktion, die Celsius in Fahrenheit umrechnet.
# Formel: Fahrenheit = Celsius * 9 / 5 + 32
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Testwerte: 0, 20 und 100 Grad Celsius.
for celsius in [0, 20, 100]:
    # TODO: Rufe die Funktion auf und gib das Ergebnis aus.
    print(f"{celsius:.2f} sind {celsius_to_fahrenheit(celsius):.2f} Fahrenheit!")
