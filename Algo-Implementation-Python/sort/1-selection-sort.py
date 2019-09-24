
def selection_sort(myList, length_of_myList):

    for i in range(0, length_of_myList-1, 1):
        index_min = i

        for j in range(i+1, length_of_myList, 1):
            if (myList[j] < myList[index_min]):
                index_min = j
        if (index_min != i):
            temp = myList[i]
            myList[i] = myList[index_min]
            myList[index_min]=temp

    return print("Selection sorted list: ", myList)

# Call Binary Search Function
myList = [3,44,38,5,15,26,27,2,46,4]
# myList = range(9)
selection_sort(myList, len(myList))
