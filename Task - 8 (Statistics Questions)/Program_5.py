import math

max_weight=int(input())
no_boxes=int(input())
mean=int(input())
std=int(input())
new_mean=mean*no_boxes
new_std=std*(no_boxes**0.5)

result=0.5*(1+math.erf((max_weight-new_mean)/(new_std*math.sqrt(2))))
print("%.4f"%result)