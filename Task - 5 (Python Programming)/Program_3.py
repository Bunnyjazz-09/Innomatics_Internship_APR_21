import re
S=input()
x = re.search(r'([a-zA-Z0-9])\1+', S)
if x:
    print(x.group(1))
else:
    print(-1)