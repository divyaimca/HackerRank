
def rev_str(s):
        
	if len(s) <= 1:
		return s[0]
	else:
		return s[-1]+rev_str(s[:-1])

print rev_str(raw_input("Enter the string:"))
