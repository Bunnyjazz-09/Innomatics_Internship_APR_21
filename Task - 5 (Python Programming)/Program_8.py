import re
N=int(input())
for _ in range(N):
    Phone_number=str(input())
    pattern=re.compile(r'[789]\d{9}$')
    if pattern.search(Phone_number):
        print("YES")
    else:
        print("NO")
