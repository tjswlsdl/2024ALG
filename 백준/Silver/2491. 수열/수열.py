N = int(input())

arr = list(map(int, input().split()))

dp_raise = [1] * N
dp_fall = [1] * N

for i in range(1,N):
    if arr[i] >= arr[i-1]:
        dp_raise[i] = dp_raise[i-1] +1
    if arr[i] <= arr[i-1]:
        dp_fall[i] = dp_fall[i-1] +1

print(max(max(dp_fall), max(dp_raise)))