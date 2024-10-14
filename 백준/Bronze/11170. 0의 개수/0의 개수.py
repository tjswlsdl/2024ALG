T = int(input())

for _ in range(T):
    cnt =0
    n, m = map(int, input().split())
    
    for i in range(n,m+1):
        w = str(i)
        cnt += w.count('0')
    
    print(cnt)