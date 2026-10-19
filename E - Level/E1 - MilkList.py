items = ["Apfel", "Brot", "Milch"]
print(items)

items.append("Reis")
print(items)

items.extend(["Tee", "Kaese"])
print(items)

items.remove("Brot")
print(items)

items.insert(1, "Wasser")
print(items)

items.pop()
print(items)