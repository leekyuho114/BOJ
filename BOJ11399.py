import sys
n=int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
array.sort(reverse=True)
result=0
for i in range(len(array)):
    result+=(i+1)*array[i]
print(result)
