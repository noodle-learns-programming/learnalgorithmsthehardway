def get_max_number_in_array(arrNumber):
    #Get the size of array
    length = len(arrNumber)
    maxValue = arrNumber[0]
    #Loop to find max value
    for i in range(0, length):
        #Compare value to find newest value
        if maxValue < arrNumber[i]:
            maxValue = arrNumber[i]

    return maxValue
        
# Example
arr = [1, 2, 3, 4, 5]
maxValue = get_max_number_in_array(arr)
print "Max value in array is: ", maxValue


