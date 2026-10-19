messungen = [
{"id": "N01", "ort": "Nord", "wert": 18.5},
{"id": "S01", "ort": "Süd", "wert": 27.0},
{"id": "W01", "ort": "West", "wert": 23.5},
{"id": "O01", "ort": "Ost", "wert": 16.0},
]

maxStation = messungen[0]

for i in range(len(messungen)):
    if maxStation.get("wert") < messungen[i].get("wert"):
        maxStation = messungen[i]
        
print(f"Waermste Station: {maxStation}")