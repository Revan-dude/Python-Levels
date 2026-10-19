text = input("Gib einen Text ein: ")

if "." not in text:
    print("Andere Datei!")
else: 
    token = str(text).split(".")[1];

    if token == "py":
        print("Python Datei!")
    else:
        print("Andere Datei!")