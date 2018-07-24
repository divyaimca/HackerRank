#!/usr/bin/python

in_str = raw_input("Enter the string:")
count = 1
arr = []
def compress(in_str):
	uniq_ = set(in_str)
	for c in uniq_:
		arr.append(c+str(in_str.count(c)))
	return "".join(arr)

print compress(in_str)
		
		
