#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    numero_columna_iter = 0
    numero_fila_iter = 0
    i = 0 #index fila
    j = 0 # index columna
    numero_hourglass_calculados = 0
    num_columnas = len(arr)
    num_fila = len(arr[0])
    numero_hourglass_fila = num_columnas-2
    lista_sumas = []
    suma=0
    n=0


    while (numero_hourglass_calculados< 4  ):
        i = 0
        j = 0
        numero_columna_iter = 0
        numero_fila_iter = 0

        num_fila = len(arr)
        for _ in range(numero_hourglass_fila):
            if numero_columna_iter > num_columnas-1:
                numero_columna_iter = 0
                numero_fila_iter = numero_fila_iter +1
            if numero_fila_iter > num_fila-1:
                numero_fila_iter = 0
            suma = sum(arr[numero_fila_iter][numero_columna_iter:numero_columna_iter+3])+arr[numero_fila_iter+1][numero_columna_iter+1] + sum(arr[numero_fila_iter+2][numero_columna_iter:numero_columna_iter+3])
            lista_sumas.append(suma)
            numero_columna_iter = numero_columna_iter +1
            suma = 0

        arr = arr [1:num_fila][0:num_columnas]
        numero_hourglass_calculados = numero_hourglass_calculados +1




    print(max(lista_sumas))
