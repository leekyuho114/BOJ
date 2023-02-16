#동전문제 greedy
#첨에 푼대로 할필요없이 나머지로 하면 쉬울걸바보야
import sys
n=int(sys.stdin.readline())
coin=[500,100,50,10,5,1]
money= 1000-n
cnt=0
for i in range(len(coin)):
    cnt+= money//coin[i]
    money%=coin[i]
print(cnt)
# while True:
#     if(money>=500):
#         money-=500
#         cnt+=1
#     else:
#         break
# while True:
#     if(money>=100):
#         money-=100
#         cnt+=1
#     else:
#         break
# while True:
#     if(money>=50):
#         money-=50
#         cnt+=1
#     else:
#         break
# while True:
#     if(money>=10):
#         money-=10
#         cnt+=1
#     else:
#         break
# while True:
#     if(money>=5):
#         money-=5
#         cnt+=1
#     else:
#         break
# while True:
#     if(money>=1):
#         money-=1
#         cnt+=1
#     else:
#         break
# print(cnt)
