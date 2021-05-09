N,M=map(int,input().split())
thickness=N//2
upper=[]
for i in range(thickness):
    string=('.|.'*((2*i)+1)).center(M,'-')
    upper.append(string)
welcome=['welcome'.upper().center(M,'-')]
lower=upper[::-1]
print('\n'.join(upper+welcome+lower))