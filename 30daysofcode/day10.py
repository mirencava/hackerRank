#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    resultado = 1
    if n == 1:
        resultado = 1
    else:
        resultado = n * factorial (n-1)

    return resultado



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    print(n)
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
    print(result)
