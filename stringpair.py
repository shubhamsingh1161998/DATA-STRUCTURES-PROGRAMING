a = ["zero", "one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twenty-one","twenty-two","twenty-three","twenty-four","twenty-five","twenty-six","twenty-seven","twenty-eight","twenty-nine","thirty","thirty-one","thirty-two", "thirty-three","thirty-four","thirty-five","thirty-six","thirty-seven","thirty-eight","thirty-nine","forty","forty-one","forty-two","forty-three","forty-four","forty-five","forty-six","forty-seven","forty-eight","forty-nine","fifty","fifty-one","fifty-two","fifty-three","fifty-four","fifty-five","fifty-six","fifty-seven","fifty-eight","fifty-nine","sixty","sixty-one","sixty-two","sixty-three","sixty-four","sixty-five","sixty-six","sixty-seven","sixty-eight","sixty-nine","seventy","seventy-one","seventy-two","seventy-three","seventy-four","seventy-five","seventy-six","seventy-seven","seventy-eight","seventy-nine","eighty","eighty-one","eighty-two","eighty-three","eighty-four","eighty-five","eighty-six","eighty-seven","eighty-eight","eighty-nine","ninety","ninety-one","ninety-two","ninety-three","ninety-four","ninety-five","ninety-six","ninety-seven","ninety-eight","ninety-nine","hundred"]
b= [2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 3, 2, 3, 4, 3, 3, 4, 4, 4, 1, 3, 2, 3, 3, 3, 2, 3, 3, 3, 1, 3, 2, 3, 3, 3, 2, 3, 3, 3, 1, 3, 2, 3, 3, 3, 2, 3, 3, 3, 1, 3, 2, 3, 3, 3, 2, 3, 3, 3, 1, 3, 2, 3, 3, 3, 2, 3, 3, 3, 2, 4, 3, 4, 4, 4, 3, 4, 4, 4, 2, 4, 3, 4, 4, 4, 3, 4, 4, 4, 2, 4, 3, 4, 4, 4, 3, 4, 4, 4, 2]
n=int(input())
sums=0
m=list(map(int,input().strip().split()))[:n]
for i in range(n):
    x=m[i]
    sums=sums+b[x]
total=0    
    
for i in range(n):
    for j in range(i,n):
        if m[i]+m[j]==sums:
            total=total+1
print(a[total])
