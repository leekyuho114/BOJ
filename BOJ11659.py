import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
pre_arr=[]
temp=0
pre_arr.append(0)
for i in range(1,n+1):
    temp+=arr[i-1]
    pre_arr.append(temp)

for i in range(m):
    s,e=map(int,input().split())
    print(pre_arr[e]-pre_arr[s-1])