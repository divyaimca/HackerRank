#!/usr/bin/python


def fib(n):
 if n <= 1:
  return n
 else:
  return fib(n-2)+fib(n-1)

def fibonacci(num):
 arr = []
 for i in range(num):
  arr.append(fib(i))
 return arr
cube = lambda x: x**3


if __name__ == '__main__':
    #n = int(raw_input())
    n = int(raw_input())
    print map(cube, fibonacci(n))
