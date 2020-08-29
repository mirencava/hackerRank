import numpy

if __name__ == '__main__':
    N, M = map(int, input().split())
    Array = numpy.array([input().split() for _ in range(N)],int)
    numpy.set_printoptions(legacy='1.13')
    print (numpy.mean(Array, axis = 1))
    print (numpy.var(Array, axis = 0))
    print (numpy.std(Array,  axis = None))
