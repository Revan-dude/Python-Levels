sorter = lambda word: len(word)

items = ["Birne", "Ei", "Apfel", "Brot"]

print(sorted(items, key=sorter))