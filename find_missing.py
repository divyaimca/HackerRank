#!/usr/bin/python

def finder(l1,l2):
	for i in l1:
		if i not in l2:
			print "{} is missing".format(i)
			l1.remove(i)
		else:
			l1.remove(i)
			l2.remove(i)




finder([1,2,3,4,5,7,6],[2,3,4,1,7])
