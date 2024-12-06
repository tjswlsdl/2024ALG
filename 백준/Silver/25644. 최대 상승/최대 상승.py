# 25214와 같은 문제.
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
dp = [0] * N # dp 초기화
small = A[0] # 
for i in range(1, N):
    small = min(small, A[i]) # 추가 될 때 마다 최솟값 찾기
    dp[i] = max(dp[i-1], A[i] - small) # 이전 최댓값 vs 이번에 구한거
print(max(dp)) 