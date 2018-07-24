
from itertools import combinations
from itertools import permutations

def permu1(string,n):
	for item in permutations(string,n):
		print ("".join(item))

#def permutation(string):
#	if 


print permu1(raw_input("Enter the string:"),3)
