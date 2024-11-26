import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+4)

dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "SK"

stone = [1,3,4]

for i in range(5,n+1):
    dp[i] = "CY"
    #dp[i] = "CY"
    
    for s in stone:
        if dp[i-s] == "CY":
            dp[i] = "SK"
            break
        
print(dp[n])