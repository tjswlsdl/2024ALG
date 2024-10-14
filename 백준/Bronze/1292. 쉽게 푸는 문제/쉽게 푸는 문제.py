start, stop = map(int, input().split())
lst = [0]

for i in range(46) :
    for _ in range(i):
        lst.append(i)
        
print(sum(lst[start:stop+1]))