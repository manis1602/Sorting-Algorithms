#ALGORITHM

"""
Step 1 : In the given list, Consider the first element as sorted and the rest of the list as unsorted.
Step 2 : Take the first element in the unsorted part(u1) and compare it with the sorted part elements (s1).
Step 3 : If u1 < s1 then insert u1 in the correct index, else leave it as it is.
Step 4 : Take the next element in the unsorted part and compare with the sorted elements.
Step 5 : Repeat step 3 and step 4 until all elements are sorted.
"""


def InsertionSort(myList):
    for index in range(1, len(myList)):
        currentElement = myList[index]
        pos = index

        # for ascending order => currentElement < myList[pos-1]
        # for descending order => currentElement > myList[pos-1]

        while currentElement < myList[pos - 1] and pos > 0:
            myList[pos] = myList[pos - 1]
            pos = pos - 1
        myList[pos] = currentElement


list1 = [34, 67, 45, 1, 98]
InsertionSort(list1)
print(list1)
