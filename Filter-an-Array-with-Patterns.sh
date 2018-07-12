#!/bin/bash

array1=()
while read line
do
 array1+=($line)
done
for c in ${array1[@]}
do
 if [[ $c = *"a"* ]] || [[ $c = *"A"* ]]; then
  :
 else
  echo $c
 fi
done
