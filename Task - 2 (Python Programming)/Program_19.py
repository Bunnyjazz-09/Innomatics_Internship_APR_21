S=set(input().split())
n=int(input())
result=False
for i in range(n): 
    N=set(input().split())
    if S.issuperset(N):
        result=True
    else:
        result=False
print(result)
