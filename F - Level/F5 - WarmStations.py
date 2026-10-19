messungen = [
{"id": "N01", "ort": "Nord", "wert": 18.5},
{"id": "S01", "ort": "Süd", "wert": 27.0},
{"id": "W01", "ort": "West", "wert": 23.5},
{"id": "O01", "ort": "Ost", "wert": 16.0},
]

border = int(input("Grenze eingeben: "))

count = 0;

for i in range(len(messungen)):
    warmth = messungen[i].get("wert")
    
    if border < warmth:
            print(messungen[i])
            count += 1
            
print(f"Insgesamte Treffer: {count}")