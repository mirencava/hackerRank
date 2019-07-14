import math

def suma(list):
    if not list:
        return 0
    else:
        return add(list[0],suma(list[1:]))

def add(x,y):
    return x + y







if __name__ == '__main__':
    list = [2,4,5,6,7]
    head = list[0]
    #tail = list [1:3] empieza en el 1 y coge hasta el 3 pero no lo incluye
    tail = list[1:]
    result = suma(list)
    print(result)
