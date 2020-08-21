# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    agenda_telefonos = {}

    if n>=1 and n<=10**5:
        for x in range(0,n):
            muestra = str(input())
            muestra_lista = muestra.split(" ")
            agenda_telefonos[muestra_lista[0]] = muestra_lista[1]


        for x in range(0,n):
            nombre = str(input())
            if agenda_telefonos.get(nombre):
                print(nombre + "=" +agenda_telefonos.get(nombre))
            else:
                print("Not found")

        
