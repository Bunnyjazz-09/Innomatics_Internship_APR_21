import math

mean,std = map(int,input().split())
scored_higher_than80=int(input())
pass_fail_thres=int(input())

result_1=0.5*(1+math.erf((scored_higher_than80-mean)/(std*math.sqrt(2))))
result_2=0.5*(1+math.erf((pass_fail_thres-mean)/(std*math.sqrt(2))))
print("%.2f"%((1-result_1)*100))
print("%.2f"%((1-result_2)*100))
print("%.2f"%((result_2)*100))