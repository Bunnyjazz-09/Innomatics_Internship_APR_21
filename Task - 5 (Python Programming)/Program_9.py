import re
from email.utils import*
N=int(input())
for _ in range(N):
    email=parseaddr(input())
    r=re.compile(r'^[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
    if r.search(email[1]):
        print(formataddr(email))