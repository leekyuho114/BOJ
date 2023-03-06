import sys
input=sys.stdin.readline

t= int(input())

for i in range(t):
    n=int(input())
    wear={}
    cnt=[]
    res = 1
    for j in range(n):
        arr=list(map(str, input().split()))
        if arr[1] in wear:
            wear[arr[1]]+=1
        else:
            wear[arr[1]]=1
    for key,value in wear.items():
        res*=(value+1)
    print(res-1)
    print(wear)