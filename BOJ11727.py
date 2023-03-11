import sys
input=sys.stdin.readline
n=int(input())
d=[0]*1002
d[1]=1
d[2]=3
for i in range(3,n+1):
    d[i]=2*d[i-2]+d[i-1]
print(d[n]%10007)
