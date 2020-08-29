# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


import sys
if __name__ == '__main__':
    valores= []
    for line in sys.stdin:
        line = map(int, line.split())
        valores.append(line)


    [print(item, end = ' ') for item in product(valores[0],valores[1]) ]


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    line = input().split()

    [print(''.join(item)) for item in sorted(permutations(line[0],int(line[1])))]

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
if __name__ == '__main__':

    S, k = input().split()
    for size in range(int(k)):
        print(*map("".join,combinations(sorted(S), size+1)),sep="\n")

from itertools import combinations_with_replacement
if __name__ == '__main__':

    S, k = input().split()

    print(*map("".join,combinations_with_replacement(sorted(S), int(k))),sep="\n")


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    line = input()

    data = [item for item in line]
    resultado= []

    [ print((len(list(item[1])),int(item[0])),end =' ') for item in groupby(data) ]

    #devuelve el número y un iterable con el mismo número cuantas veces se repite en el original


from itertools import combinations

N = int(input())
L = input().split()
K = int(input())
C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)

print("{0:.3}".format(len(list(F))/len(C)))
