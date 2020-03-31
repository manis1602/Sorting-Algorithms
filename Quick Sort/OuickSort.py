"""
ALGORITHM:

Step 1: Select the pivot element.
Step 2: Find out the correct position of the pivot element in the list by rearranging it.
Step 3: Divide the list based on pivot element.
Step 4: Sort the list recursively.

"""
"""
Condition for DESCENDING order:
    while left <= right and list1[left] >= pivot
        left = left + 1
    while left <= right and list1[right] <= pivot:
        right = right - 1
"""


def pivotPlace(myList, first, last):
    pivot = myList[first]
    left = first + 1
    right = last
    while True:
        while left <= right and myList[left] >= pivot:
            left = left + 1
        while left <= right and myList[right] <= pivot:
            right = right - 1
        if right < left:
            break
        else:
            myList[left], myList[right] = myList[right], myList[left]
    myList[first], myList[right] = myList[right], myList[
        first]  # If last element is taken as pivot element, then swap pivot element with left index value.
    return right


def QuickSort(list1, first, last):
    if first < last:
        pivotIndex = pivotPlace(list1, first, last)
        QuickSort(list1, first, pivotIndex - 1)
        QuickSort(list1, pivotIndex + 1, last)


myList = [30, 45, 21, 2, 78, 43, 56]
QuickSort(myList, 0, len(myList) - 1)
print(myList)
