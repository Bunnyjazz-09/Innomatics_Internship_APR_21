import numpy

N,M=map(int,input().split())
array=numpy.array([input().split() for _ in range(N)],float)
print(numpy.mean(array,axis=1))
print(numpy.var(array,axis=0))
std=numpy.std(array)
print(numpy.around(std, 11))
