num1 = int(input("Gib eine Zahl ein: "))
num2 = int(input("Gib eine Zahl ein: "))
num3 = int(input("Gib eine Zahl ein: "))

if num1 > num2 and num1 > num3:
    print(f"Die Erste Nummer({num1}) ist die Groesste!")
elif num2 > num1 and num2 > num3:
    print(f"Die Zweite Nummer({num2}) ist die Groesste!")
elif num3 > num2 and num3 > num1:
    print(f"Die Dritte Nummer({num3}) ist die Groesste!")
        
            