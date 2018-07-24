#!/usr/bin/python

s1 = raw_input("Enter string1:")
s2 = raw_input("Enter string2:")


def soln(str1,str2):
  l1 = list(str1.strip())
  l2 = list(str2.strip())
  len1=len(l1)
  #print l1
  #print l2
  l3 = []
  status = False
  if len(l1) != len(l2):
   return status
  else:
   for i in range(len(l1)+1):
    for c in l1:
     if c in l2:
      l3.append(True)
      l1.remove(c)
      l2.remove(c)
#   assert (len1 == len(l3))
  if len1 == len(l3):
   status = True
  return status


print soln(s1,s2)


