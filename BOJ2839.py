import sys
input = sys.stdin.readline

n=int(input())
res=0
while True:
    if(n%5 == 0):
        res+=n//5
        print(res)
        break
    n-=3
    res+=1
    if n == 0:
        print(res)
        break
    elif n<0:
        print(-1)
        break
