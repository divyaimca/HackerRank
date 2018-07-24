
def selection_sort(arr):
	swapped = False
	for backfill in range(len(arr),0,-1):
	
		posMax = 0
		for location in range(1,len(arr)+1):
			if arr[location] > arr[posMax]:
				posMax = location
				
		arr[posMax],arr[backfill]=arr[backfill],arr[posMax]
				
				
				

	return arr
			
			












ar = input("Enter the array:")
print selection_sort(list(ar))
