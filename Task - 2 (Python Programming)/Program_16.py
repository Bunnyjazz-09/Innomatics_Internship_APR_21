n=int(input())
A=set(input().split())
N=int(input())
for i in range(N):
    l=input().split()
    B=input().split()
    if l[0]=="intersection_update":
        A.intersection_update(set(B))
    elif l[0]=="update":
        A.update(set(B))
    elif l[0]=="symmetric_difference_update":
        A.symmetric_difference_update(set(B))
    elif l[0]=="difference_update":
        A.difference_update(set(B))
print(sum(map(int,A)))