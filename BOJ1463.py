import sys
input = sys.stdin.readline
n=int(input())
a=[0]*1000001
a[1]=0

for i in range(2,n+1):
    # a[i] = min(a[i-1],a[i//3],a[i//2])
    a[i]=a[i-1]
    if(i%2==0):
        a[i]=min(a[i],a[i//2])
    if(i%3==0):
        a[i]=min(a[i],a[i//3])
    a[i]+=1

print(a[n])
