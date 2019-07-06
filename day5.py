#!/bin/python3

import math
import os
import random
import re
import sys

def printMultiplos(n):
    for x in range(1, 11):
        print(str(n) + ' x ' + str(x) + ' = ' + str(n*x))


if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=20:
        printMultiplos(n)
