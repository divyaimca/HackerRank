#!/usr/bin/python



def seq_search(arr,item):
	pos = 0
	found = False
	stopped = False
	while pos < len(arr) and not found and not stopped:
		if arr[pos] == item:
			found = True
		else:
			if arr[pos] > item:
				stopped = True
			else:
				pos += 1
	return found







array1 = input("Array:")
toSearch = input("toSearch:")

print seq_search(array1,toSearch)

