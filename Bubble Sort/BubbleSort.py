def BubbleSort(myList):
    for i in range(len(myList)):
        swapped = False
        for j in range(0, len(myList) - i - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
                swapped = True
        if not swapped:  # same as swapped == False
            break


inputList = [54, 2, 89, 45, 67, 135, 77, 89, 12]
BubbleSort(inputList)
print(inputList)
