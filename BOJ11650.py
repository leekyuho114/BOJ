import sys

n = int(sys.stdin.readline())
array=[]
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
# 그 이런식이면 그냥 y순으로 정렬한거밖에 안됨
# array.sort(key = lambda x:x[0])
# array.sort(key = lambda x:x[1])
array.sort(key = lambda x:(x[0],x[1]))

for i in range(n):
    print(array[i][0], array[i][1])
