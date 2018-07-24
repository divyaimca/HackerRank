#!/usr/bin/python

def sum_pair(arr,k):
	pairs = []
	for i in arr:
		if k-i in arr:
			if (k-i,i) in pairs:
				continue
			else:
				pairs.append((i,k-i))

	return [x for x in set(pairs)]
			




print sum_pair([1,2,3,2,4,0,5],7)
