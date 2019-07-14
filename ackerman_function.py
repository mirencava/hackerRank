def A(m, n, s="%s"):
    print (s % ("A(%d,%d)" % (m, n)))
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1, s)
    n2 = A(m, n - 1, s % ("A(%d,%%s)" % (m - 1)))
    return A(m - 1, n2, s)

if __name__ == '__main__':
    print('introduce un entero')
    m = int(input())
    print('introduce un entero')
    n= int(input())
    print(A(m,n))
