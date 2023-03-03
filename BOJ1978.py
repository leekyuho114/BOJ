import sys
import math
n=int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
res=0

for i in range(n):
    #숫자 하나당
    cnt=0
    if array[i] == 1:
        continue
    for j in range(2, int(math.sqrt(array[i]))+1):
        if( array[i]%j == 0 ):
            cnt=1
            break
    if (cnt==0):
        res+=1

print(res)