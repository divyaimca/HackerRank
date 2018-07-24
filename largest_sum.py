#!/usr/bin/python


def largest_sum(arr):
	sum = 0
	sums = [0]
	for i in arr:
		if i < 0:
			sum = 0
			continue
		else:
			sum += i
			if sum > sums[-1]:
				sums.append(sum)

	return max(sums)


print largest_sum([2,3,-1,-2,0,10,100,-9,23,98])
			
