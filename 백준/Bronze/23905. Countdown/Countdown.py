def count_k_countdown(arr, N, K):
    count = 0
    for i in range(N - K + 1):
        if arr[i:i+K] == list(range(K, 0, -1)):
            count += 1
    return count

def count_k_countdown_large(arr, N, K):
    count = 0
    consecutive_descending = 0
    
    for i in range(N):
        if arr[i] == K:
            consecutive_descending = 1
        elif i > 0 and consecutive_descending > 0 and arr[i] == arr[i-1] - 1:
            consecutive_descending += 1
        else:
            consecutive_descending = 0
        
        if consecutive_descending == K:
            count += 1
            
    return count

# 입력 받기
T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if N > 1000:
        result = count_k_countdown_large(arr, N, K)
    else:
        result = count_k_countdown(arr, N, K)
    
    print(f"Case #{case}: {result}")
