station1 = {
    "location": "Nord",
    "value": 18.5,
    "unit": "°C"
}

station2 = {
    "location": "Labor",
    "value": 68.0,
}

print(f"Ort: {station1.get("location")}, Wert: {station1.get("value")}, Einheit: {station1.get("unit", "unbekannt")}")
print(f"Ort: {station2.get("location")}, Wert: {station2.get("value")}, Einheit: {station2.get("unit", "unbekannt")}")