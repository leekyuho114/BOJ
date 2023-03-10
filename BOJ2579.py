#그리디로 풀었는데 틀렸음
import sys
input = sys.stdin.readline
n= int(input())
arr=[0 for _ in range(n+3)]
d=[0]*400
for i in range(1,n+1):
    arr[i]=(int(input()))

d[1]=arr[1]
d[2]=arr[1]+arr[2]
for i in range(3,n+1):
    d[i]=max(d[i-2]+arr[i], d[i-3]+arr[i-1]+arr[i])

print(d[n])