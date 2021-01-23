#!/bin/bash
for filename in "$@";do
	echo $filename
	awk '(NR==1 || NR==6 || NR==21 || NR==81 || NR==201)' $filename 
done
