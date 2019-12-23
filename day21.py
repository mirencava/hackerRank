#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberofswapscount=0
# Write Your Code Here
for i in range(n):
    numberofswaps = 0

    for j in range(n-1):
        if a[j]>a[j+1]:
            item=a[j+1]
            a[j+1]=a[j]
            a[j]=item
            numberofswaps=numberofswaps+1
            numberofswapscount=numberofswapscount+1
    if numberofswaps==0:
        break

print('Array is sorted in ' + str(numberofswapscount)+ ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[len(a)-1]))
