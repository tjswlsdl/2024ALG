n, k = map(int, input().split())

pascal = [[1]*i for i in range(1,n+1)]

for i in range(2,n):
    for j in range(1,i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        
print(pascal[n-1][k-1])