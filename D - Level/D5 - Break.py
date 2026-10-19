sum = 0
count = 0

while True:
    count += 1

    num = int(input("Gib eine Zahl ein bis null: "))
    
    sum += num;
    
    if num == 0:
        break
    
print(f"Die Summe: {sum}, Wieviele Zahlen: {count}")