#!/bin/bash

array1=()
while read line
do
 array1+=($line)
done
 array1+=($line)
 
 echo ${array1[@]/[A-Z]/.}
