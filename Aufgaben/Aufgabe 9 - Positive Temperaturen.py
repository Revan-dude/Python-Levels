# Aufgabe: Erzeuge mit einer List Comprehension eine Liste aller Werte groesser als 0.
# Berechne den Durchschnitt der ausgewaehlten Temperaturen.
temperatures = [-4.5, 0.0, 3.2, 8.0, -1.1, 5.5]

# TODO: Waehle die strikt positiven Temperaturen aus.
positive_temperatures = [value for value in temperatures if value > 0]

# TODO: Berechne den Durchschnitt der ausgewaehlten Temperaturen.

def calc_average(values):
    return sum(values) / len(values)
average = calc_average(temperatures)

print("Original:", temperatures)
print("Positive Temperaturen:", positive_temperatures)
# TODO: Gib den Durchschnitt mit zwei Nachkommastellen aus.
print(f"Durchschnitt: {average:.2f}")