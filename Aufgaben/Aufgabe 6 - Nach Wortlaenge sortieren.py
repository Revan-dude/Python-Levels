# Aufgabe: Sortiere die Woerter nach ihrer Laenge.
# Verwende sorted und eine lambda-Funktion als key.
words = ["Wasser", "Ei", "Birne", "Brot", "Tee"]

# TODO: Erzeuge eine neue, nach Wortlaenge sortierte Liste.

sorter = lambda word: len(word)
sorted_words = sorted(words, key=sorter)

print("Original:", words)
print("Sortiert:", sorted_words)
