import math

ticket_left=int(input())
students=int(input())
mean=float(input())
std=float(input())
new_mean=mean*students
new_std=std*(students**0.5)

result=0.5*(1+math.erf((ticket_left-new_mean)/(new_std*math.sqrt(2))))
print("%.4f"%result)