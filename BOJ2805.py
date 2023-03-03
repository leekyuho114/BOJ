#이코테 떡볶이문제랑 같은 문제
import sys
def search_len(array,target,start,end):
    res=0
    while start<=end:
        total=0
        mid= (start+end)//2
        for i in range(n):
            if(array[i]-mid > 0):
                total += arr[i] - mid
        if(total<target):
            end=mid-1
        else:    
            res=mid
            start=mid+1
    print(res)

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
search_len(arr,m,0,max(arr))