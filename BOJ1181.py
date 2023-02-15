import sys
n=int(sys.stdin.readline())
array= []
for i in range(n):
    array.append(str(sys.stdin.readline()))

set_array=list(set(array))
set_array.sort()
set_array.sort(key=len)

for i in range(len(set_array)):
    print(set_array[i],end='')

#set 파이썬 자료형 집합이므로 집합으로 형변환해주면
#중복사라짐