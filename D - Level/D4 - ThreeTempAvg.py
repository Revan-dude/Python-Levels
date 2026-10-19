temperatureList = [];

for i in range(0, 3):
    temperatureList.append(float(input(f"Gib Zahl {i + 1} ein: ")))
    
average = 0.0;

for i in range(len(temperatureList)):
    average += temperatureList[i]

average = average / len(temperatureList)

print(temperatureList)
print(f"Der Durchschnitt lautet: {average:.2f}!")
    
