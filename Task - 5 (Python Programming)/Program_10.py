import re
N=int(input())
case=False
for i in range(N):
    s=input()
    r=re.compile(r'(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})\b')
    output=r.search(s)
    if '{' in s:
        case=True
        continue
    if '}' in s:
        case=False
        continue
    elif case:
        for output in r.findall(s):
            print(output)