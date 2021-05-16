n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))

mean_X=sum(X)/n
mean_Y=sum(Y)/n
std_X=(sum([(i - mean_X)**2 for i in X]) / n)**0.5
std_Y=(sum([(i - mean_Y)**2 for i in Y]) / n)**0.5
sum1=0

for i in range(n):
    sum1+=(X[i]-mean_X)*(Y[i]-mean_Y)
pearson=sum1/(n*std_Y*std_X)

print("%.3f"%pearson)