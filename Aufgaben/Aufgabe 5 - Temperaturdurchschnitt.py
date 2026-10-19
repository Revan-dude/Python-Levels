# Aufgabe: Berechne den Durchschnitt der drei Testtemperaturen.
# Gib ihn mit genau zwei Nachkommastellen aus.
temperatures = [18.5, 20.0, 21.5]

# TODO: Berechne den Durchschnitt aus der Liste.
average = sum(temperatures) / len(temperatures)

print("Temperaturen:", temperatures)
# TODO: Formatiere den Durchschnitt bei der Ausgabe mit zwei Nachkommastellen.
print(f"Durchschnitt: {average:.2f}")
