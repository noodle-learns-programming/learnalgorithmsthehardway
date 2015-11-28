
def bubble_sort(arr_list):
	length = len(arr) - 1
	swapped = True
	while swapped:
		swapped = False
		for i in range(0, length):
			if arr_list[i] > arr_list[i+1]:
				tmp = arr_list[i]
				arr_list[i] = arr_list[i+1]
				arr_list[i+1] = tmp
				swapped = True
	return arr_list

arr = [1, 9, 5, 2, 3, 6]
result = bubble_sort(list(arr))

print 'unsort array: ', arr
print 'sorted array: ', result
