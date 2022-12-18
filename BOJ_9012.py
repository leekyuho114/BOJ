import sys
n = int(sys.stdin.readline())
stack=[]
result=[]
def VPS(self):
    cnt=0
    for i in range(len(self)):
        temp=self.pop()
        if((i==0 and temp=='(') or (i==len(self)-1 and temp==')')):
            return 'NO'
        if(temp==')'):
            cnt+=1
        elif(temp=='('):
            cnt-=1
        if(cnt<0):
            return 'NO'
    if(cnt==0):
        return 'YES'
    else:
        return 'NO' 

for i in range(n):
    ps=sys.stdin.readline()
    for j in range(len(ps)-1):
        stack.append(ps[j])

    result.append(VPS(stack))
    stack.clear()

for k in result:
    print(k)

"""
이거 stack에 다넣고 시작하는게 아니라
검사를 stack으로 하는거임 몽총아 다시하도록
근데 예제는 되는데 왜틀린고징..
"""