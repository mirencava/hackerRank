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
