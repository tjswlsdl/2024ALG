N = int(input())
num = list(map(int, input().split()))
k = int(input())


index = N // k
arr = []


for i in range(0,N,index) :
    arr = num[i:i+index]
    arr.sort()
    
    for j in arr:
        print(j, end =' ')