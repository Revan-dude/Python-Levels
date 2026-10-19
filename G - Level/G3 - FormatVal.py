def format_val(val, unit="°C", count=1):
    return f"{val:.{count}f}{unit}"

valueTester = [24.9, 25.0, 30.0]

print("-------------- Test 1 --------------")

for i in range(len(valueTester)):
    print(format_val(valueTester[i]))
    


print("-------------- Test 2 --------------")

for i in range(len(valueTester)):
    print(format_val(valueTester[i], "°F"))
    
print("-------------- Test 2 --------------")

for i in range(len(valueTester)):
    print(format_val(valueTester[i], count=6))