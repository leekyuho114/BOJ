import sys
import heapq
input = sys.stdin.readline
n=int(input())
q=[]
#최초 n까지는 heap 에 push
for i in range(n):
    num_list = list(map(int,input().split())) 
    for k in num_list:
        if(i<1):
            heapq.heappush(q,k)
        else:
            if(q[0]<k):
                heapq.heappop(q)
                heapq.heappush(q,k)
print(q[0])
    