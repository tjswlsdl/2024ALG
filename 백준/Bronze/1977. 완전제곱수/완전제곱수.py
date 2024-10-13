import math

N = int(input())
M = int(input())
sum = 0
lst = []
for i in range(N,M+1) :
    
    if math.sqrt(i) % 1 == 0:
        sum += i
        lst.append(i)

if len(lst) == 0:
    print('-1')    
else:        
    print(sum)
    print(min(lst))