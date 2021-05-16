import math

b,g=map(float,input().split())
n=6
P_S=b/(b+g)
result=0
for i  in range(3,7):
    result=result+((math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*(P_S**i)*     (1-P_S)**(n-i))
print("%.3f"%result)