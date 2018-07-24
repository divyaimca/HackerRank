#!/usr/bin/python

s_to_r = raw_input("Enter the string to reverse:").strip()

rev_str=[]
for i in range(len(s_to_r)-1,-1,-1):
	rev_str.append(s_to_r[i])


print "".join(rev_str)
