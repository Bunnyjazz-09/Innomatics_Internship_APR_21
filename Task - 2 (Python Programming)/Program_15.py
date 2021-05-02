n=int(input())
English=set(map(int,input().split()))
b=int(input())
French=set(map(int,input().split()))
count=0
for i in ((English - French)|(French - English)):
    count+=1
print(count)