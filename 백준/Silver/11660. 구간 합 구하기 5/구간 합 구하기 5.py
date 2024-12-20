import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mat = []
for _ in range(N):
    line = list(map(int, input().split()))
    mat.append(line)
    
dp = [ [0]*(N+1) for i in range(N+1) ]    

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + mat[i-1][j-1]

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    res = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(res)

