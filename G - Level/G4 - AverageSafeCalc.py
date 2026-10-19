def average(values=[]):
    if len(values) == 0:
        return None
    else:
        return sum(values) / len(values)
    
testValue1 = [10, 20, 30]
testValue2 = [7]
testValue3 = []

print(average(testValue1))
print(average(testValue2))
print(average(testValue3))