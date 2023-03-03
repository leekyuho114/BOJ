import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

stack=[]
res=[]
cnt=0
no_flag=0
for i in range(len(arr)):
    if not stack:
         cnt+=1
         stack.append(cnt)
         res.append("+")
    while arr[i]>stack[-1]:
            cnt+=1
            stack.append(cnt)
            res.append("+")
    if(arr[i]==stack[-1]):   
        stack.pop()
        res.append("-")
    else:
        no_flag=1
        break
if(no_flag):
     print("NO")
else:
    for i in range(len(res)):
         print(res[i])