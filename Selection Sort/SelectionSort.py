def SelectionSort(inputArr):
    size = len(inputArr)
    for index in range(size):
        tempIndex = index
        for j in range(index + 1, size):
            if inputArr[tempIndex] > inputArr[j]:
                tempIndex = j
        # Swapping the values in the array
        inputArr[index], inputArr[tempIndex] = inputArr[tempIndex], inputArr[index]
    return inputArr


arr = [45, 24, 78, 95, 34, 88, 911, 110, 5, 200]
print(SelectionSort(arr))
