T = int(input())

for _ in range(T):
    p = int(input())
    name = []
    price = []
    for i in range(p):
        b,a = input().split()
        name.append(a)
        price.append(int(b))
        
    idx = price.index(max(price))
    print(name[idx])
