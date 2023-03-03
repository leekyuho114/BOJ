import sys

def binary(x,array):
    start=0
    end=len(array)-1
    result=0
    while start<=end:
        mid= (start+end)//2
        if array[mid]==x:
            result+=1
            start=mid+1
        elif array[mid]<x:
            start=mid+1
        else:
            end=mid-1
    print(result, end= " ")

n= int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
m= int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
arr1.sort()

for i in range(len(arr2)):
    binary(arr2[i],arr1)
