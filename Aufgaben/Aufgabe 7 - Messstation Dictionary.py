# Aufgabe: Lies die Werte aus dem Dictionary aus, aendere die Temperatur
# und gib danach den neuen Temperaturwert aus.
station = {
    "name": "Nord",
    "temperatur": 18.5
}

# TODO: Gib Name und aktuelle Temperatur einzeln aus.

print(f"Name: {station["name"]}, Temperatur: {station.get("temperatur")}")

# TODO: Aendere die Temperatur auf 20.0.

station["temperatur"] = 20.0

# TODO: Gib die aktualisierte Temperatur aus.

print(f"Temperatur: {station.get("temperatur")}")
