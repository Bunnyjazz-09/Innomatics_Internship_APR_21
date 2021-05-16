import numpy

N,M=map(int,input().split())
array=numpy.array([input().split() for _ in range(N)],int)
minimum=numpy.min(array,axis=1)
print(numpy.max(minimum))
