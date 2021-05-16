import numpy
N,M,P=map(int,input().split())
matrix=numpy.array([input().split() for j in range(N)],int)
matri=numpy.array([input().split() for j in range(M)],int)
print(numpy.concatenate((matrix, matri), axis = 0))