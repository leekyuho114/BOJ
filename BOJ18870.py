#자기보다 작은 좌표 개수
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))
temp=arr.copy()
arr= list(set(arr))
arr.sort()
for i in range(n):
    print(bisect_left(arr,temp[i]),end=" ")
#이거 코드 너무 오래걸림 근데 bisect logN임