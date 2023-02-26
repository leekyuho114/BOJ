#파이썬에서는 ㅂ2ㅜ동소수점 오차가 나서 정확하지 않다고 한다. 
#decimal 을 사용하는 방법도 있고 암튼 문제가 생기면 소수점문제에서는
#이부분도 잘 체크해보자
import sys
x, y = map(int,sys.stdin.readline().split())
z=int((y*100/x))
start=0
end=1000000000
result=0
if z>=99:
    result=-1
else:
    while start<=end:
        mid = (start+end)//2
        if int(((y+mid)*100/(x+mid))) < z+1:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

print(result)