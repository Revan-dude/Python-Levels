num = int(input("Gib eine Zahl ein!"))

if num < 0:
    print("Nicht richtige Zahl!")
else:
    
    while num is not -1:
        print(num)
        num -= 1
    
    print("Start!")