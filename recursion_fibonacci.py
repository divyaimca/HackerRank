
	

def fib(n):
	if n <= 1:
		return 1
	else:

		return fib(n-2)+fib(n-1)


num=input("Enter the number:")
for i in range(num):
	print fib(i) 
