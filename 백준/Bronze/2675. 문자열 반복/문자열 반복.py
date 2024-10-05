import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    S = list(S)

        
    for j in range(len(S)):
        print(S[j]*R, end = '')
    print('')
