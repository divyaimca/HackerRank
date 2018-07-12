#!/bin/bash

read count
A=()
for i in $count
do
 read num
 A+=($num)
done

printf "%s\n" ${A[@]} | sort | uniq -u
