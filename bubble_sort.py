myList = [1,50, 13, 15, 48,6]
end = len(myList)-1
while True:
    swapped = -1
    for i in range(0, end):
        if myList[i] > myList[i+1]:
            temp = myList[i]
            myList[i] = myList[i+1]
            myList[i+1] = temp
            swapped = i
    if swapped == -1:
        break
print(myList)
    
            
    
