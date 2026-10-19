numbers = [4, 9, 12, 7, 15]

border = int(input("Gib eine Zahl als Grenze ein: "))
val = -1

for i in range(len(numbers)):
    if numbers[i] >= border:
        val = numbers[i]
        break;
    
if val == -1:
    print("Keinen Treffer!")
else:
    print(f"Treffer: {val}")