import re
T=int(input())
for _ in range(T):
    s=input()
    r=re.compile(r'.*(.).*\1')
    if r.search(s):
        print("Invalid")
    else:
        print("Valid")