def warm_values(values, border=25.0):
    out = []
    
    for i in range(len(values)):
        val = values[i]

        if val > border:
            out.append(val)
            
    return out

testValue1 = [18.5, 27.0, 23.5]
testValue2 = []

print(warm_values(testValue1))
print(warm_values(testValue1, 23))
print(warm_values(testValue2))