# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
import sys
if __name__ == '__main__':
    valores= []
    for line in sys.stdin:
        line = map(int, line.split())
        valores.append(line)


    [print(item, end = ' ') for item in product(valores[0],valores[1]) ]
