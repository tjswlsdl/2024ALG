N, M = map(int, input().split())
chapters = [list(map(int, input().split())) for _ in range(M)]

dp = [0] * (N + 1)

for i in range(M):
    for j in range(N, chapters[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-chapters[i][0]] + chapters[i][1])
        
print(dp[N])