import math
import os
import random
import re
import sys

def isWeirdOrNot(N):
    resto = N%2

    if resto !=0 :
        print('Weird')
    else :
        if N>=2 and N<=5:
            print('Not Weird')
        elif N>=6 and N<=20:
            print('Weird')
        else :
            print('Not Weird')



if __name__ == '__main__':
    N = int(input())
    isWeirdOrNot(N)
