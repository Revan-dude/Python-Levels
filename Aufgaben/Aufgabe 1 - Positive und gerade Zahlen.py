# Aufgabe: Waehle mit einer List Comprehension nur strikt positive gerade Zahlen aus.
numbers = [-8, 3, 0, 12, -2, 7, 4]

# TODO: Erzeuge hier eine neue Liste mit den passenden Zahlen.
positive_even_numbers = [number for number in numbers if number % 2 == 0 and number > 0]

print("Original:", numbers)
print("Ergebnis:", positive_even_numbers)
