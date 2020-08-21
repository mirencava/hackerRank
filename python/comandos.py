
def comandos (comando, resultado):

    lista_comandos= ['insert','print','remove','append','sort','pop','reverse']

    if comando[0] == lista_comandos [0]:
        resultado.insert(int(comando[1]),int(comando[2]))
    if comando[0] == lista_comandos [1]:
        print(resultado)
    if comando[0] == lista_comandos [2]:
        resultado.remove(int(comando[1]))
    if comando[0] == lista_comandos [3]:
        resultado.append(int(comando[1]))
    if comando[0] == lista_comandos [4]:
        resultado.sort()
    if comando[0] == lista_comandos [5]:
        resultado.pop()
    if comando[0] == lista_comandos [6]:
        resultado.reverse()




if __name__ == '__main__':
    resultado = []
    N = int(input())
    for i in range (N):
        comando = input().split()
        comandos(comando,resultado)
