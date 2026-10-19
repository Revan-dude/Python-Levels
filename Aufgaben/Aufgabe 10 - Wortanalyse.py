# Aufgabe: Teile den Satz in Woerter, waehle Woerter mit mindestens 4 Zeichen
# aus und sortiere sie mit sorted und lambda nach ihrer Laenge.
sentence = "Python macht Programmieren spannend und kreativ"

# TODO: Teile den Satz mit split() in eine Wortliste.
words = sentence.split(" ");

# TODO: Erzeuge eine neue Liste mit Woertern, die mindestens 4 Zeichen lang sind.
long_words = [word for word in words if len(word) > 4]

# TODO: Sortiere diese Woerter nach ihrer Laenge.
sorter = lambda word: len(word)
sorted_words = sorted(words, key=sorter)

print("Satz:", sentence)
print("Ausgewaehlte Woerter:", long_words)
print("Nach Laenge sortiert:", sorted_words)
