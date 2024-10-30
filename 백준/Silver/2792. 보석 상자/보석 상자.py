import sys
input=sys.stdin.readline

N,M=map(int,input().split())
L=[]

for i in range(M):
    L.append(int(input()))
    
start=1  # mid 값이 0이 되는것을 막기 위해 1로 시작한다.
end=max(L) #end 값은 리스트 L의 최대값이다.
answer=0 #정답을 담을 변수

while start<=end:
    mid=(start+end)//2
    sum = 0
    for i in range(len(L)):
        sum+=L[i]//mid
        if L[i]%mid!=0:
            sum+=1
    if sum>N:
        start=mid+1
    else:
        end=mid-1
        answer=mid
print(answer)