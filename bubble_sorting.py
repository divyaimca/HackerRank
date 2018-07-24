import time

def bubble_sort(arr):
	swapped = False
	swap_count = 1
	while swap_count <= len(arr) :
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
				swapped = True
		swap_count += 1
	return arr



ar = input("Enter the array:")
print bubble_sort(list(ar))
			
	
