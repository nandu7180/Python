dict1 = {"0ne": 1, "Three": 3, "Five": 5, "Two": 2, "Four": 4}

myList = []
for k, v in sorted(dict1.items()):
    myList.append(v)

length = len(myList) - 1
while True:
    swapped = 1
    for i in range(0, length):
        if myList[i] > myList[i + 1]:
            temp = myList[i]
            myList[i] = myList[i + 1]
            myList[i + 1] = temp
            swapped = i

    if swapped == 1:
        break

print "Bubble Sort by Values", myList

myList.sort()
print "Using Sort keyword", myList
