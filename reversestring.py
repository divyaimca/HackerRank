#!/usr/bin/python
stri = raw_input("Enter the string:")

print stri

rev = []

for i in range(len(stri)-1,-1,-1):
 rev.append(stri[i])

print "".join((rev))

