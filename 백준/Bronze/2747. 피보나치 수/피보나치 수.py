N = int(input())
list = [0,1]

for i in range(N):
    list.append(list[i] + list[i+1])
    #print(list[])
        
print(list[N])