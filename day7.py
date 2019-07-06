#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    resultado = ""

    for x in range(0,n):
        if x == 0:
            letrafinal = str(arr[x])
        else:
            resultado = resultado + str(arr[-x]) +  " "
    resultado = resultado  + letrafinal


    print (resultado)


   
