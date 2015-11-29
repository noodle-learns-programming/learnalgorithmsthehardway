def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = -1

    while first <= last and found == -1:
        mid = (first + last)/2;
        if alist[mid] == item:
            found = mid
        #If the value need to search in the right
        elif item > alist[mid]:
            first  = mid + 1
        #If the value need to search in the left
        else:
            last = mid - 1
    return found

#a list be sorted by asc
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print 'Found indexOf at: ', binarySearch(alist, 3)

