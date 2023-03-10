import sys
def pw_search(start,end,arr,target):
    while start<=end:
        mid=(start+end)//2
        if(arr[mid][0] == target):
            print(arr[mid][1])
            break
        elif(arr[mid][0]>target):
            end=mid-1
        else:
            start=mid+1


input =sys.stdin.readline
n,m= map(int, input().split())
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))

arr.sort(key = lambda x:x[0])
for i in range(m):
    target=str(input().strip())
    pw_search(0,n,arr,target)

