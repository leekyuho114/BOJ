import sys
n= int(sys.stdin.readline())
array=[]
for i in range(n):
    array.append(str(sys.stdin.readline()).strip())
for i in range(n):
    cnt=0
    res=0
    for j in range(len(array[i])):
        if array[i][j]=='O':
            cnt+=1
            res+=cnt
        else:
            cnt=0
    print(res)
