text = input("Gib einen Text ein: ")
token = input("Gib ein suchToken ein: ")
count = 0

for i in range(0, len(text)):
    if token == text[i]:
        count += 1
        
print(count)