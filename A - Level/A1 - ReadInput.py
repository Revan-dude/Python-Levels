name = input("Gib deinen Namen ein: ");
age = input("Gib dein Alter ein: ");

if(name.isalpha() and age.isdigit()):
    print(f"Hallo {name}, nächstes Jahr bist du {int(age) + 1} Jahre alt.");