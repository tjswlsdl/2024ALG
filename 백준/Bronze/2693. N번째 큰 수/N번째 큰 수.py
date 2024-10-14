T = int(input())
lst = []

for _ in range(T):
    a = list(map(int,input().split()))
    a.sort()
    print(a[-3])
