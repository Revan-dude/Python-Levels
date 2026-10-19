age = int(input("Gib dein Alter ein: "))
begleitung = str(input("Begleitung? (ja/nein): ").strip().upper())

if age < 16:
    if begleitung == "NEIN":
        print("Zugang Verweigert")
    else:
        if age < 15:
            print("Zugang Verweigert")
        else:  
            print("Zugang Erlaubt!")
else:
    print("Zugang Erlaubt!");