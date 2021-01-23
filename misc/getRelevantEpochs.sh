#!/bin/bash
for filename in "$@";do
	echo $filename
	awk 'BEGIN {FS=","} NR==5 || NR==9 {print $4}' $filename
	#awk 'BEGIN {FS=","} NR==1 || NR==5 || NR==9 {print $1,$4}' $filename # also show epoch
	#awk '(NR==1 || NR==6 || NR==21 || NR==81 || NR==201)' $filename # show complete line
done
