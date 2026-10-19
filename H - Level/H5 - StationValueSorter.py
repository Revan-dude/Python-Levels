values = [
{"id": "N01", "ort": "Nord", "wert": 18.5},
{"id": "S01", "ort": "Süd", "wert": 27.0},
{"id": "W01", "ort": "West", "wert": 23.5},
{"id": "O01", "ort": "Ost", "wert": 16.0},
]

def sort_values(values, reverseVal=False):
    sorter = lambda val: val.get("wert")
    
    return sorted(values, key=sorter, reverse=reverseVal)

print(values)
print(sort_values(values))
print(sort_values(values, True))