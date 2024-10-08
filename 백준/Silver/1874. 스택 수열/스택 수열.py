import sys
input = sys.stdin.readline
N = int(input())
numlist = [i for i in range(1,N+1)]
count = 0
stack = [-1]   # bottom
res = []
Fesability = True
for i in range(N):
    iscomplete = False
    need = int(input())
    while not iscomplete:
        if stack[-1] == need:
            res.append('-')
            del stack[-1]
            iscomplete = True
        elif need < stack[-1]: # Can't make array
            Fesability = False
            break
        else:
            while need != stack[-1]:
                stack.append(numlist[count])
                res.append('+')
                count += 1
if Fesability:
    for s in res:
        print(s)
else:
    print('NO')