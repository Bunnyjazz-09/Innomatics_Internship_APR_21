if __name__ == '__main__':
    s = input()
    dig=False
    up=False
    lo=False
    alpha=False
    alnum=False
for i in range(len(s)):
    if(s[i].isdigit()):
        dig=True
    elif(s[i].isupper()):
        up=True
    elif(s[i].islower()):
        lo=True
if ( (dig == True) | (lo== True) | (up== True) ):
    alnum=True
if ( (lo == True) | (up == True) ):
    alpha=True
print(str(alnum)+"\n"+str(alpha)+"\n"+str(dig)+"\n"+str(lo)+"\n"+str(up))