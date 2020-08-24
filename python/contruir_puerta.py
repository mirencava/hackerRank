# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
if __name__ == '__main__':

    dimensiones = ""
    for line in sys.stdin:
        dimensiones= line

    dimensiones = dimensiones.split()
    N= int(dimensiones[0])
    M= int(dimensiones[1])

    # rallas= indice + (indice+1)
    # puntos = rallas * 2

    #el primer . se escribre en M-3/2

    medio_wel = int((M-3)/2)
    fila_welcome = int(((N-1)/2)+1)
    n=1
    arriba = True
    abajo = False
    for line in range(N):

        if line == fila_welcome-1:
            print (('-'* (medio_wel-2)) + 'WELCOME' +('-'* (medio_wel-2) ) )
            abajo = True
            arriba = False

        else:
            medio = int((M-(3*n))/2)
            print (('-'*medio) + ('.' + '|'+'.')*(n) +('-'*medio) )

        if arriba:
            n=n+2
        else:
            n=n-2



N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): # 1 3 5
    print('-'*((M-3*i)//2) + '.|.'*i + '-'*((M-3*i)//2)) #Enter Code Here // division cogiendo el entero
print('-'*((M-7)//2)+'WELCOME'+'-'*((M-7)//2)) #Enter Code Here
for i in range(N-2,-1,-2):
    print('-'*((M-3*i)//2) + '.|.'*i + '-'*((M-3*i)//2)) #Enter Code Here
