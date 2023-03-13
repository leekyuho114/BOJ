import sys
input = sys.stdin.readline

def z_loc(n, start, r, c):
    temp=n
    for i in range(temp-1):
        if (r >= 2**(n-1)):
            if(c >= 2**(n-1)):
                start = start + (((2**n)**2)//4)*3
                r = r-2**(n-1)
                c = c-2**(n-1)
            else:
                start = start + (((2**n)**2)//2)
                r = r-2**(n-1)
        else:
            if(c >= 2**(n-1)):
                start = start + (((2**n)**2)//4)
                c = c-2**(n-1)
        n-=1

    return start + r*2 + c

n, r, c = map(int,input().split())
print(z_loc(n, 0 , r, c))