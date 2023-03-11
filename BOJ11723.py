import sys
input=sys.stdin.readline
m = int(input())
s = set()
for i in range(m):
    cmd = list(map(str, input().strip().split()))
    if cmd[0] == "add":
        s.add(int(cmd[1]))
    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == "all":
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif cmd[0] == "empty":
        s.clear()