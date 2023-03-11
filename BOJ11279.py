import sys
import heapq
input=sys.stdin.readline
n = int(input())
q=[]
for i in range(n):
    k = int(input())
    if(k==0):
        if(q):
            print(-heapq.heappop(q))
        else:
            print(0)
    if(k>0):
        heapq.heappush(q,-k)