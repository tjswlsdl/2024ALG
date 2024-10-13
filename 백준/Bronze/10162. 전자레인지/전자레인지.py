T = int(input())
a= 0
b=0
c=0
if T % 10 == 0:
    a = T // 300
    b = (T-300*a) // 60
    c = (T - 300*a - 60*b) // 10
    if a >= 1:
        T = T - 300*a
        b = T // 60
        if b >= 1:
            T = T - 60*b
            c = T // 10
     
    print(f'{a} {b} {c}')
    
        
else :
    print('-1')