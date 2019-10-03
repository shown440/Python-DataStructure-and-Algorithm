
def insertion_sort(myList, length_of_myList):

    for i in range(1, length_of_myList, 1):
        
        item = myList[i]
        j = i-1
        
        while(j>=0 and myList[j]>item):

            myList[j+1] = myList[j]
            j = j-1
        myList[j+1] = item

    return print("Insertion sorted list: ", myList)

# Call insertion sort Function
myList = [3,44,38,5,47,15,36,26,27,2]
# myList = range(9)
insertion_sort(myList, len(myList))
