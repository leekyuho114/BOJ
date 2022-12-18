import sys
stack = []
n = int(sys.stdin.readline())
result =0
for i in range(n):
    num=int(sys.stdin.readline())
    if (num==0):
        stack.pop()
    else:
        stack.append(num)

for i in range(len(stack)):
    result+=stack.pop()

print(result)