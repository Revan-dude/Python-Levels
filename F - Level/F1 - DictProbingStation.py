station = {
    "id": "N01",
    "location": "Nord",
    "value": 18.5,
    "activeStatus": True
}

print(f"Ortsname: {station["location"]}, Messwert: {station["value"]:.2f}, Anzahl der Eintraege: {len(station)}")