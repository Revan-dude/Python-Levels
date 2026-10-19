inputStr = str(input("Gib einen Text ein: "))

middle = len(inputStr) // 2
slice1 = inputStr[:middle]
slice2 = inputStr[middle:]

print(f"Erste Haelfte: {slice1}")
print(f"Zweite Haelfte: {slice2}")