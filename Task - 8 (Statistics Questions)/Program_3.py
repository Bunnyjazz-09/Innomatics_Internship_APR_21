import math

mean,std=map(float,input().split())
t=float(input())
t1,t2=map(float,input().split())
result_1=0.5*(1+math.erf((t-mean)/(std*math.sqrt(2))))
result_2=0.5*(1+math.erf((t2-mean)/(std*math.sqrt(2))))-0.5*(1+math.erf((t1-mean)/(std*math.sqrt(2))))
print("%.3f"%result_1)
print("%.3f"%result_2)
