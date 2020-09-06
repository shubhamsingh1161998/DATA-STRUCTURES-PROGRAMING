mport random
import re
import sys

# Complete the repeatedString function below.
s=input()
n=int(input())
d=s.lower()
d=d*100000000
a='a'
count=0 
for i in range(n):
    if d[i]==a:
        count=count+1
    else:
        continue 
print(count)          


