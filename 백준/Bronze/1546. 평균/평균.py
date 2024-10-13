N = int(input())
sum = 0
score = list(map(int, input().split()))
na = max(score)

for i in range(N):
    sum += score[i]/na *100

result = round((sum/N),6)
print(result)
    