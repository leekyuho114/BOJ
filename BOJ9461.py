#뒤집 하얀 삼각형은 파랑삼각 두개랑 접
#반대도 성립
import sys
input=sys.stdin.readline
t=int(input())
d=[0]*102
for i in range(t):
    n=int(input())
    d[1]=1
    d[2]=1
    d[3] = 1
    d[4]=2
    d[5]=2
    for j in range(6,n+1):
                d[j]=d[j-1]+d[j-5]
    print(d[n])