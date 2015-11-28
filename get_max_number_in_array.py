def get_max_number_in_array(arrNumber):
    maxValue = arrNumber[0]
    #Loop to find max value
    for val in arrNumber:
        #Compare value to find newest value
        if maxValue < val:
            maxValue = val

    return maxValue
        
# Example
arr = [1, 2, 3, 4, 5]
maxValue = get_max_number_in_array(arr)
print "Max value in array is: ", maxValue


