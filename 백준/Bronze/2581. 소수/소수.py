N = int(input())
M = int(input())

lst =[]

for i in range(N,M+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                lst.append(i)
            break
        
if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print('-1')