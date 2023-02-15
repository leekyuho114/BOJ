from collections import deque
import sys
n,m = map(int, sys.stdin.readline().split())
idx = list(map(int,sys.stdin.readline().split()))
cnt=0
dq= deque([i for i in range(1,n+1)])
for i in idx:
    while True:
        if (dq[0]==i):
            dq.popleft()
            break
        else:
            if(len(dq)/2>dq.index(i)):#위치가 큐의 앞쪽
                while dq[0]!=i:
                    dq.append(dq.popleft())
                    cnt+=1
            else:#위치가 큐의 뒤쪽
                while dq[0]!=i:
                    dq.appendleft(dq.pop())
                    cnt+=1
print(cnt)
