n = int(input())
lst = []

for i in str(n):
    lst.append(int(i))
    
lst.sort(reverse= True)

for i in lst:
    print(i,end='')