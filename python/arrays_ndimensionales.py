import numpy

if __name__ == '__main__':
    N, M = map(int, input().split())
    Array = numpy.array([input().split() for _ in range(N)],int)
    print(numpy.max(numpy.min(Array, axis=1), axis=0))
