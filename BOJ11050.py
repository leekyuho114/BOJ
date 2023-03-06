import sys
input = sys.stdin.readline
n,k=map(int,input().split())
res=1
if k > n-k:
    k=n-k
tn=n
tk=k
for i in range(k):
    res*=tn
    tn-=1
for i in range(k):
    res/=tk
    tk-=1

print(int(res))