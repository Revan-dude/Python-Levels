text = input("Gib einen Text ein: ")
backWardText = text[::-1]

if backWardText.upper() == text.upper():
    print("Es ist ein Palindrom!")
else:
    print("Es ist kein Palindrom!")