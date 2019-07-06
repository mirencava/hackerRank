# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys
from sys import stdin



if __name__ == '__main__':
    n = int(input())
    agenda_telefonos = {}
    lines = sys.stdin.readlines()
    if n>=1 and n<=10**6 and len(lines)<=10**6 and len(lines)>=1 :
        for x in range(0,n):

             muestra_lista = lines[x].split(" ")
             agenda_telefonos[muestra_lista[0].strip()] = muestra_lista[1].split("\n")[0]
        for x in range(n,len(lines)):

            nombre = lines[x].strip()
            if nombre in agenda_telefonos:
               print('%s=%s' % (nombre, agenda_telefonos[nombre]))
            else:
                print("Not found")
