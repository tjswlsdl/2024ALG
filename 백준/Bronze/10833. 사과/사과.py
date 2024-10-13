T = int(input())
lst=[]
sum = 0
for _ in range(T):
    ppl, apple = map(int, input().split())
    rest = int(apple - (apple//ppl)*ppl)
    sum += rest

print(sum)    