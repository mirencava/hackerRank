# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import re
import sys

if __name__ == '__main__':
    T = int(input())

    for x in range(0, T):
        cadena = str(input())
        cadenaEven = ""
        cadenaOdd = ""
        n=0
        for i in cadena:
            if n==0:
                cadenaEven = cadenaEven + i
            elif n%2==0:
                cadenaEven = cadenaEven + i
            else:
                cadenaOdd = cadenaOdd + i
            n = n +1

        resultado = cadenaEven + " " + cadenaOdd
        print(resultado)
