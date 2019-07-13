def mc91(n):
    print(str(n) + ' mc91')
    if n > 100:
        print(n-10)
        return n - 10

    else:
        return mc91(mc91(n + 11))



if __name__ == '__main__':
    print('introduce un entero')
    n = int(input())
    result = mc91(n)
