#!/bin/python3

import math
import os
import random
import re
import sys

def decimalToBinary(n,resultado):
    if n > 1:
        decimalToBinary(n//2,resultado)
    resultado.append(str(n%2))



if __name__ == '__main__':
    n = int(input())
    resultado = []
    decimalToBinary(n,resultado)
    binario =''.join(resultado)
    unos = binario.split('0')
    contador = []
    count = 0

    for item in unos:
        count = 0
        for uno in item :
            count = count + 1
        contador.append(count)

    print(max(contador))


# def binary(n):
#     bin=[]
#     while n>1:
#         bin.append(n%2)
#         n=n//2
#         if n==0 or n==1:
#             bin.append(n)
#     return bin


# #!/bin/python3
#
# import sys
#
#
# n = int(input().strip())
#
# i, t, M = 1, 0, 0
# while i <= n:
#     if n & i != 0:
#         t += 1
#         M = max(M, t)
#     else:
#         t = 0
#     i <<= 1
#     print(i)
#
# print(M)
#
