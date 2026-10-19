def is_hot(temperature, border=25.0):
    return temperature >= border

valueTester = [24.9, 25.0, 30.0]


print("-------------- Test 1 --------------")

for i in range(len(valueTester)):
    print(is_hot(valueTester[i]))
    


print("-------------- Test 2 --------------")

for i in range(len(valueTester)):
    print(is_hot(valueTester[i], 30))
    
print("-------------- Test 3 --------------")
    
for i in range(len(valueTester)):
    print(is_hot(valueTester[i], 35))