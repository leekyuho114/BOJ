import sys
n=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())
task=n//k
result_arr=[]
for i in range(k):
    temp=array[i*task:(i+1)*task]
    temp.sort()
    result_arr+=temp
for i in range(n):
    print(result_arr[i],end=" ")