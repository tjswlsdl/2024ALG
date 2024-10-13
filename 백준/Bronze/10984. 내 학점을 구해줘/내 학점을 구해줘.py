T = int(input())

for _ in range(T):
    n = int(input())
    num = 0
    sum = 0
    for _ in range(n):
        a, b = map(float ,input().split())
        num += int(a)
        sum += float(a)*float(b)
    sum = round(sum/num,1)
    print(num, sum)
    