import sys
input=sys.stdin.readline
n,m=map(int, input().split())
s1=set()
s2=set()
for i in range(n):
    s1.add(input().strip())
for i in range(m):
    s2.add(input().strip())

res = sorted(list(s1&s2))
print(len(res))
for i in res:
    print(i)