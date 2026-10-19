# Aufgabe: Pruefe, ob jedes Testwort vorwaerts und rueckwaerts gleich ist.
# Gross- und Kleinschreibung soll beim Vergleich keine Rolle spielen.
test_words = ["Rentner", "Python"]

for word in test_words:
    # TODO: Vergleiche das Wort mit seiner umgedrehten Version.
    if word == word[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    # TODO: Gib passend zu is_palindrome eine Meldung fuer das Wort aus.
    print(word, is_palindrome)
