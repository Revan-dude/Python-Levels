def celsius_to_fahrenheit(celsius):
    if type(celsius) == int:
        return celsius * 9 / 5 + 32
    else:
        return 0
    
valueTester = [0, 20, -40]

for i in range(len(valueTester)):
    print(celsius_to_fahrenheit(valueTester[i]))