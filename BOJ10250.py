import sys
input=sys.stdin.readline

def findRoom(h,w,n):
    floor=n%h
    dist=(n//h)+1
    if(n%h==0):
        floor=h
        dist-=1
    return floor*100 + dist

T=int(input())
for i in range(T):
    h,w,n=map(int,input().split())
    print(findRoom(h,w,n))