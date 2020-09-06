def longestsubarray(arr, n, k): 
    current_count = 0
    max_count = 0
  
    for i in range(0, n, 1): 
        if (arr[i] % k != 0): 
            current_count += 1
        else: 
            current_count = 0
        max_count = max(current_count,  
                            max_count) 
      
    return max_count 
x=int(input())
for j in range(0,x):
    a,b=input().split()
    n=int(a)
    k=int(b)
    arr=list(map(int,input().strip().split()))[:n]
    z=longestsubarray(arr, n, k)
    if z>0:
        print(z)
    else:
        print(-1)
