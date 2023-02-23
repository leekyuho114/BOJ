#시간 초과 때문에 set으로 바꿔서 풀었음
import sys

n = int(sys.stdin.readline())
arr1=set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
for i in range (len(arr2)):
    result=0
    if arr2[i] in arr1:
        result=1
    print(result)

#이분탐색으로 풀어보기 binary search