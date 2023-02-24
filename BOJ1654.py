import sys
k,n= map(int,sys.stdin.readline().split())
array=[]
for i in range(k):
    array.append(int(sys.stdin.readline()))
start =1
end= max(array)
answer=0
while start<=end:
    #n 값 계산
    # 충족하면 저장하고 최적의값 계속 계산
    # 충족못하면 저장 x
    result=0
    mid=(start+end)//2
    for i in range(k):
        result+= array[i]//mid
    if result<n:
        end= mid-1
    else:
        answer=mid
        start=mid+1

print(answer)