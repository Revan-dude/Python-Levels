side1 = input("Gib die Länge der ersten Seite ein: ");
side2 = input("Gib die Länge der zweiten Seite ein: ");

if(side1.isdigit() and side2.isdigit()):
    if(int(side1) > 0 and int(side2) > 0):
        area = int(side1) * int(side2);
        sides = (int(side1) + int(side2)) * 2;
        print(f"Die Fläche des Rechtecks beträgt {area} Quadratmeter.");
        print(f"Der Umfang des Rechtecks beträgt {sides} Meter.");