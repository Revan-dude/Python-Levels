text = input("Gib einen Text ein: ")
outText = ""

for i in range(0, len(text), 2):
    outText += text[i]
    
print(outText)