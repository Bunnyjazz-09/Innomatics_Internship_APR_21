import math
p,n=map(int,input().split())
P_S=p/100
result_1=0
result_2=0
for i  in range(0,3):
    result_1=result_1+((math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*          (P_S**i)*(1-P_S)**(n-i))
for i  in range(2,11):
    result_2=result_2+((math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*          (P_S**i)*(1-P_S)**(n-i))
print("%.3f"%result_1)
print("%.3f"%result_2)