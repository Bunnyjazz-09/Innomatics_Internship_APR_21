import re
S=str(input())
r=re.findall(r"[^aiueo]([aiueoAIUEO]{2,})(?=[^aiueo])",S)
if r:
    for s in r:
        print(s)
else:
    print(-1)