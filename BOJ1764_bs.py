import sys
input=sys.stdin.readline
n,m=map(int, input().split())
ddo=[]
bdo=[]
cnt=0
res=[]
for i in range(n):
    ddo.append(input().strip())
for i in range(m):
    bdo.append(input().strip())

ddo.sort()
bdo.sort()
for i in range(n):
    start = 0
    end = len(bdo)-1
    target=ddo[i]
    while start<=end:
        mid=(start+end)//2
        if(target==bdo[mid]):
            cnt+=1
            res.append(target)
            break
        elif(target>bdo[mid]):
            start=mid+1
        else:
            end=mid-1

print(cnt)
for i in range (len(res)):
    print(res[i])