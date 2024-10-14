lst = []
sum = 0

for i in range(9):
    h = int(input())
    sum += h
    lst.append(h)
lst.sort()

fake=[]    

for i in range(9):
    for j in range(i+1, 9):
        
        if len(fake) == 2 :
            continue
        
        if(sum-(lst[i]+lst[j]) == 100):    
            fake.append(lst[i])
            fake.append(lst[j])
            
for i in lst:
    if i in fake:
        continue
    print(i)
        