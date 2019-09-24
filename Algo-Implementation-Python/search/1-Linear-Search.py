
def linear_search(myList, length_of_myList, searchable_number):
    i = 0
    while(i!=length_of_myList):
        if myList[i] == searchable_number:
            return print(searchable_number, " is found at position ", i+1)
        i=i+1
    return print(searchable_number, " is not found")

myList = [10,40,30,100,60,55,20]
linear_search(myList, len(myList), 100)
