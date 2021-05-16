import numpy

N,M=map(int,input().split())
array=numpy.array([input().split() for _ in range(N)],int)
sum=numpy.sum(array,axis=0)
print(numpy.prod(sum))