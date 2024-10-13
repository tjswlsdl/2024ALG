T = int(input())


for _ in range(T):
    N = int(input())
    school = []
    soju = []
    
    for i in range(N):
        a, b = input().split()
        school.append(a)
        soju.append(int(b))
        
    idx = soju.index(max(soju))
    print(school[idx])