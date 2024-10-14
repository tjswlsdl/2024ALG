T = int(input())


for i in range(T):
    tmp = 0
    clas = list(map(int, input().split()))
    score = clas[1:clas[0]+1]
    score.sort()
    
    for j in range(1, clas[0]):
        if (score[j] - score[j-1]) > tmp:
            tmp = score[j] - score[j-1]
    
    print(f'Class {i+1}')
    print(f'Max {max(score)}, Min {min(score)}, Largest gap {tmp}')