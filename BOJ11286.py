import sys
import heapq
input=sys.stdin.readline
n = int(input())
q=[]
for i in range(n):
    k = int(input())
    if(k==0):
        if(q):
            value, sign = heapq.heappop(q)
            if(sign==1):
                print(value)
            else:
                print(-value)
        else:
            print(0)
    elif(k>0):
        heapq.heappush(q,(k,1))
    else:
        heapq.heappush(q,(-k,-1))
