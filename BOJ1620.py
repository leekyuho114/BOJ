import sys
input=sys.stdin.readline
n,m= map(int,input().split())
pckmon=dict()
for i in range(n):
    name=str(input().strip())
    pckmon[name]=i+1
    pckmon[i+1]=name
for i in range(m):
    target=input().strip()
    if(not "A"<=target[0]<="Z"):
        target=int(target)
    if(type(target)==str):
        print(pckmon[str(target)])
    else:
        print(pckmon[target])