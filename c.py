s=['<','{','[','(']
d=['>','}',')',']']
k=str(input())
a=[]
sums=0
b=[]
c=[]
m=0
n=0
for x in k:
    a.append(x)
for i in range(len(s)):
    for j in range(len(a)):
        if a[j]==s[i]:
            m=m+1
    b.append(m) 
    m=0
for i in range(len(d)):
    for j in range(len(a)):
        if a[j]==d[i]:
            n=n+1
    c.append(n) 
    n=0
if sum(b)==sum(c):
    for i in range(len(s)):
        sums=sums+abs(b[i]-c[i])
    print(sums)    
else:
    print("Impossible")
