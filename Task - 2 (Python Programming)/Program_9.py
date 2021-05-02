M=int(input())
a=set(map(int,input().split()))
N=int(input())
b=set(map(int,input().split()))
c= sorted(list((a.difference(b)).union(b.difference(a))))
for i in c:
    print(i)