def merge_the_tools(string, k):
    # your code goes here
    anterior=0
    resultado= []
    for i in range(k,len(string)+1,k):
        resultadofinal = []
        resultado = string[anterior:i]
        for elemento in resultado:
            if elemento not in resultadofinal:
                resultadofinal.append(elemento)

        print(''.join(resultadofinal))
        anterior=i




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
