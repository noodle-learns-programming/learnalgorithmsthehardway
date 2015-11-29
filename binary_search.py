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

def binarySearchWithRecursive(alist, item, first=0, last=None):
    last = len(alist) - 1 if last is None else last
    mid = (first + last)/2;
    if first > last:
        return -1
    if alist[mid] == item:
        return mid
    elif item > alist[mid]:
        return binarySearchWithRecursive(alist, item, mid + 1, last)
    else:
        return binarySearchWithRecursive(alist, item, first, mid -1)

    

#a list be sorted by asc
alist = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
print 'Found indexOf at: ', binarySearchWithRecursive(alist, 5)

