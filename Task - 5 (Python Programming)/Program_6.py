import re
N=int(input())
for _ in range(N):
    text=input()
    if " || " in text:
        print(re.sub(" || "," or ",text))
    elif " && " in text:
        print(re.sub(" && "," and ",text))
    else:
        print(text)