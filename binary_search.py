#!/usr/bin/python

note="""Only on Sorted array"""

def binary_search(arr,item):
	first = 0
	last = len(arr)-1
	found = False
	
	while first <= last and not found:
		mid = (first+last)/2
		if arr[mid] == item:
			found = True
		else:
			if arr[mid] < item:
				first = mid
			else:
				mid = last	
		first += 1


	return found

print note
ar = input("Enter array:")
it = input("Enter item to search:")
print binary_search(ar,it)



			
