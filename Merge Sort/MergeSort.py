def MergeSort(myList):
    if len(myList) > 1:
        # Dividing the list at the mid point
        mid = len(myList) // 2
        leftList = myList[:mid]
        rightList = myList[mid:]
        # Recursively calling the MergeSort Function on the divided list
        MergeSort(leftList)
        MergeSort(rightList)
        i, j, k = 0, 0, 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                myList[k] = leftList[i]
                i = i + 1
                k = k + 1
            else:
                myList[k] = rightList[j]
                j = j + 1
                k = k + 1
        while i < len(leftList):
            myList[k] = leftList[i]
            i = i + 1
            k = k + 1
        while j < len(rightList):
            myList[k] = rightList[j]
            j = j + 1
            k = k + 1


list1 = [55, 12, 34, 98, 43, 2, 43]
MergeSort(list1)
print(list1)
