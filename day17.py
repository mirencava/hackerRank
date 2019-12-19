#!/bin/python3

import sys


S = input().strip()
try:
    y = int(S)
    print(y)
except ValueError:
    y = None
    print('Bad String')


