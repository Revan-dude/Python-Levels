items = [3, 1, 3, 2, 1, 4]
newList = []

for i in range(len(items)):
    if newList.count(items[i]) == 0:
        newList.append(items[i])
        
print(items)
print(newList)