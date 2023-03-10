import sys
input=sys.stdin.readline
t=int(input())
f=[[0 for _ in range(2)] for _ in range(42)]
f[0]=[1,0]
f[1]=[0,1]
test=[]
for i in range(t):
    test.append(int(input()))
k=max(test)
for i in range(2,k+1):
    f[i][0]=(f[i-1][0] + f[i-2][0])
    f[i][1]=(f[i-1][1] + f[i-2][1])

for i in range(t):
    print(f[test[i]][0],f[test[i]][1])

