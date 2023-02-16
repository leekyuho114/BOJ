import sys
n=int(sys.stdin.readline())
array=[]
for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    array.append([int(a), b])

array.sort(key= lambda x : x[0])
for i in range(n):
    print(array[i][0],array[i][1])