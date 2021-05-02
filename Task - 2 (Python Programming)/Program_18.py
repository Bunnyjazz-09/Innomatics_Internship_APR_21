T=int(input())
for i in range(T):
    x=map(int,input().split())
    for _ in x:
        A=set(input().split())
    y=map(int,input().split())
    for _ in y:
        B=set(input().split())
    if A.issubset(B):
        print(True)
    else:
        print(False)