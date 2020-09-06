n=int(input())
a=[]
a=list(map(int,input().strip().split()))[:n]
k=min(a)
b=[]
c=[]
for i in range(n):
    if a[i]==k:
        b.append(i)
for i in range(len(b)-1):
    m=0
    m=b[i+1]-b[i]
    c.append(m)
print(min(c))  
