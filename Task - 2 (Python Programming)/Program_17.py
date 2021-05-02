from collections import Counter
K=int(input())
l=list(map(int,input().split()))
counts=Counter(l)
for i, count in counts.items():
    if count!=K:
        print(i)
