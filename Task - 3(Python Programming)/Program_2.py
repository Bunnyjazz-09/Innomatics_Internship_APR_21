import math 
AB=int(input())
BC=int(input())
AC=math.sqrt(AB**2 + BC**2)
BM=AC/2.0
BN=BC/2.0
theta=math.acos(BN/BM)
print(str(round(math.degrees(theta))) + chr(176))
