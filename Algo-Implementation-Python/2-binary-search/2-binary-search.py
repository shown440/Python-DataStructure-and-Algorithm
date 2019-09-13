
def binary_search(myList, length_of_myList, searchable_number):
    left_index = 0
    right_index = length_of_myList-1

    while(left_index <= right_index):
        mid_index = (left_index + right_index) // 2

        if myList[mid_index] == searchable_number:
            return print(searchable_number, "is found at index position ", mid_index)
            # print(mid_index)

        if myList[mid_index] < searchable_number:
            left_index = mid_index+1
        else:
            right_index = mid_index-1

    return print(searchable_number, " is not found")

# Call Binary Search Function
myList = [1,2,3,4,5,6,7,8]
# myList = range(9)
binary_search(myList, len(myList), 3)
