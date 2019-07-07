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
