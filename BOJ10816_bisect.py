from bisect import bisect_left,  bisect_right
import sys

n= int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
m= int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
arr1.sort()

def count_by_range(array,value):
    right_index=bisect_right(array,value)
    left_index=bisect_left(array,value)
    return right_index-left_index


for i in range(len(arr2)):
    print(count_by_range(arr1,arr2[i]), end= " ")