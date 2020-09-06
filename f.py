import math
x,p=map(int,input().split())
a=list(map(int,input().strip().split()))[:x]
sums=0
for i in range(x):
    sums=sums+1/math.pow(p,a[i])
m=math.pow(p,sum(a))
k=m*sums
n=k%116000000812
print(n)
