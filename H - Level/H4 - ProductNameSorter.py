products = [
{"name": "Stift", "preis": 1.5, "bestand": 20},
{"name": "Heft", "preis": 2.0, "bestand": 8},
{"name": "Mappe", "preis": 3.5, "bestand": 12},
{"name": "Block", "preis": 2.0, "bestand": 15},
]

sorter = lambda product: product.get("name")

sortedList = sorted(products, key=sorter)

for i in range(len(sortedList)):
    product = sortedList[i]
    
    print(f"Name: {product.get("name")}, Price: {product.get("preis"):.2f}")

print(products)