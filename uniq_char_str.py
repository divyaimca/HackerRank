

st = raw_input("String:")

def uniq_str(stri):
	uniq_ = set(stri)
	if len(uniq_) != len(stri):
		return False
	else:
		return True	

print uniq_str(st)
	
