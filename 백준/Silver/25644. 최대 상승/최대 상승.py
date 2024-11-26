import sys
input = sys.stdin.readline

N = int(input())
high = 0
result = 0

ANA = list(map(int, input().split()))
    
for i in range(N-1,-1,-1):
    high = max(high, ANA[i])
    result = max(result, high -ANA[i] )
    
print(result)
