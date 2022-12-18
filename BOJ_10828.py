import sys
stack=[] #일단 그냥 리스트로 풀어보기 -> 이렇게 풀면될듯
result=[]
def push(a):
    stack.append(a)

def empty(self):
    if(self[-1]):
        None

n = int(sys.stdin.readline())

for i in range(n):
    str=sys.stdin.readline().split()
    if(str[0]=="push"):
        push(int(str[1]))
    elif(str[0]=="pop"):
        if(len(stack)==0):
            result.append(-1)
        else:
            result.append(stack.pop())
    elif(str[0]=="size"):
        result.append(len(stack))
    elif(str[0]=="empty"):
        if(len(stack)==0):
            result.append(1)
        else:
            result.append(0)
    elif(str[0]=="top"):
        if(len(stack)==0):
            result.append(-1)
        else:
            result.append(stack[len(stack)-1]) #stack[-1]은 top 원소 가져오기만함

for j in range(len(result)):
    print(result[j])