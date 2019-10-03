
def bubble_sort(myList, length_of_myList):

    for i in range(0, length_of_myList, 1):

        for j in range(0, length_of_myList-i-1, 1):

            if (myList[j] > myList[j+1]):
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1]=temp

    return print("Bubble sorted list: ", myList)

# Call bubble sort Function
myList = [3,44,38,5,47,15,36,26,27,2]
# myList = range(9)
bubble_sort(myList, len(myList))
