messungen = [
{"id": "N01", "ort": "Nord", "wert": 18.5},
{"id": "S01", "ort": "Süd", "wert": 27.0},
{"id": "W01", "ort": "West", "wert": 23.5},
{"id": "O01", "ort": "Ost", "wert": 16.0},
]

searchWord = input("Suchbegriff eingeben: ")

value = -1

for i in range(len(messungen)):
    if searchWord.upper() == str(messungen[i].get("id")).upper():
        print(messungen[i])
        value = 0
        break
    
if value == -1:
    print("Nicht gefunden!")