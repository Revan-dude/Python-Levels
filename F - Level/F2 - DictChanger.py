station = {
    "id": "N01",
    "value": 18.5,
    "active": True
}

station["value"] = 20;
station["location"] = "Nord";
station.pop("active")

print(station)