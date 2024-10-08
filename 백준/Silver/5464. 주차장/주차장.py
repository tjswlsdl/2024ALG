n,m=map(int,input().split()) #주차공간n 차량m
Rs=[0] #단위무게당요금 i 번쨰
Wk=[0] #차량의 무게 i 번째
for _ in range(n):
    Rs.append(int(input()))
for _ in range(m):
    Wk.append(int(input()))
I=[] #차 오고가는거 큐
for _ in range(2*m):
    I.append(int(input()))
money=0 #주차료 = 차량의 무게 X 그 자리 값
visit=[0]*(n+1)
while I:
    for i in range(n):
        if visit[i+1]==0:
            Y=i+1
            break
        else: Y=-1
    #빈자리 Y번째칸 근데? 없으면 -1
    if Y==-1: #빈자리없으면 나가는차바로찾기
        for i in range(len(I)):
            if I[i]<0:
                break
        X=I.pop(i)
    else:
        X=I.pop(0)
    #X에 i차가 들어왓는지나갔는지저장
    if X>0:
        money += Rs[Y] * Wk[X]
        visit[Y]=X
    else:
        for i in range(1,n+1):
            if visit[i]== -X:
                visit[i]=0
                break

print(money)