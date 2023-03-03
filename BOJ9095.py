import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
d=[0]*100
d[1]=1
d[2]=2
d[3]=4

for i in range(4,max(arr)+1):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for i in range(n):
    print(d[arr[i]])