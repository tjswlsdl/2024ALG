import sys
input = sys.stdin.readline

n,m = map(int, input().split())


# 체스판 만들기
chess = []
res = []

for _ in range(n):
    chess.append(input().rstrip())
        


# 체스판 검사하기
## 일단 체스판 잘라준다 7을 빼주고 돌려야 8*8 으로 자를수 있다.
## ex) m,n = 11 -> 0~7 / 1~8 / 2~9 / 3~10 이렇게 4번 돌아간다.
for x in range(n-7):
    for y in range(m-7): 
        idx_w = 0
        idx_b = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
## 이제 체스판이 두종류(왼쪽 위가 하양 or 검정) 인 것을 이용하자
                if (i+j)%2 == 0: # 짝수일때 
                    if chess[i][j] != 'W' : # 시작점이 B이면
                        idx_w += 1
                    else:
                        idx_b += 1
                else : # 홀수일때
                    if chess[i][j] != 'W':
                        idx_b += 1
                    else:
                        idx_w += 1
        res.append(idx_w)
        res.append(idx_b)
print(min(res))


