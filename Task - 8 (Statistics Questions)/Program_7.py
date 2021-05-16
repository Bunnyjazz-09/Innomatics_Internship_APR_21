n=int(input())
mean=int(input())
std=int(input())
dist_percent=float(input())
z_value=float(input())

sample_std=std/(n**0.5)

A=mean-(sample_std*z_value)
B=mean+(sample_std*z_value)

print("%.2f"%A)
print("%.2f"%B)