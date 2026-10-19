# Aufgabe: Sammle die Zeichen an Index 1, 3, 5 usw. in einem neuen String.
# Testtext: Das Ergebnis soll sich fuer "Python" ueberpruefen lassen.
text = "Python"
result = ""

# TODO: Gehe mit range und len ueber die passenden Indizes.

for i in range(1, len(text), 2):
    result += text[i]

print("Text:", text)
print("Jedes zweite Zeichen ab Index 1:", result)
