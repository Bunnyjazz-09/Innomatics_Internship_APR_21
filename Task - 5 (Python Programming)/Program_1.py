import re
T=int(input())
for i in range(T):
    N=input()
    pattern=re.compile(r'^[-+]?[0-9]*[.][0-9]+$')
    print(bool(pattern.search(N)))