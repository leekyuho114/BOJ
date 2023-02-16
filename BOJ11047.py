#비슷한 동전문제 greedy
import sys
n, k = map(int,sys.stdin.readline().split())
array=[0]*n
cnt=0
for i in range(n):
    array[i]=int(sys.stdin.readline())
for i in range(n-1,-1,-1):
    cnt+=k // array[i]
    k%=array[i]
print(cnt)