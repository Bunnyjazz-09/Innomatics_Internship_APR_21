import numpy

N=int(input())
array=numpy.array([input().split() for _ in range(N)],float)
print(numpy.round(numpy.linalg.det(array),2))