import re
S=str(input())
k=str(input())
pattern=re.compile(k)
m=pattern.search(S)
if m:
    while m:
        print("({}, {})".format(m.start(),m.end()-1))
        m=pattern.search(S,m.start()+1)
else:
    print("(-1, -1)")