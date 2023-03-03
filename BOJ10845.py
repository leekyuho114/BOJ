from collections import deque
import sys
n= int(sys.stdin.readline())
queue = deque([])
for i in range(n):
    cmd =str(sys.stdin.readline().strip())
    if  "push" in cmd:
        queue.append(int(cmd.split()[1]))
    elif "pop" in cmd:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif "size" in cmd:
        print(len(queue))
    elif "empty" in cmd:
        if queue:
            print(0)
        else: 
            print(1)
    elif "front" in cmd:
        if queue:
            print(queue[0])
        else: 
            print(-1)
    elif "back" in cmd:
        if queue:
            print(queue[-1])
        else:
            print(-1)
    
    
