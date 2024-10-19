import sys
#import numpy as np
input = sys.stdin.readline



N = int(input())
#answer = []
#num_list = [ i for i in range(1,N+1)]
stack = []
op = []
cnt = 1
temp = True
for _ in range(N):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        op.append('+')
    
    
    if stack[-1] >= num :
        stack.pop()
        op.append('-')
    
    else :
        temp = False
        break

if temp == False :
    print('NO')
else:
    for i in op:
        print(i)