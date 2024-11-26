import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [0] *(n+3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4,n+3):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # dp[i] = sum(dp[i-3:i])
    print(dp[n])
    
    



