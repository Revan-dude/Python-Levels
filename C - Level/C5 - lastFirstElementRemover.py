text = input("Gib einen Text ein: ")

if len(text) < 2:
    print("Zu kurz!")
else:
    text = text[1:len(text) - 1]
    
    print(text);