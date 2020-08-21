if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    lista= sorted(set(lista))
    print (lista[len(lista)-2])