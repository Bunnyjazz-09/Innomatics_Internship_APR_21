n=5
x=[95,85,80,70,60]
y=[85,95,70,65,70]
sum_x=0
sum_y=0
sum_x2=0
sum_xy=0
for i in range(n):
    sum_xy+=(x[i]*y[i])
    sum_x+=x[i]
    sum_y+=y[i]
    sum_x2+=(x[i])**2
    
    
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y / n) - b * (sum_x / n)
print(round(a+b*80,3))