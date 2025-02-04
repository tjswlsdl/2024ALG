import sys
input = sys.stdin.readline


def find(x):
    for i in range(n-x+1):
        for j in range(m-x+1):
            if square[i][j] == square[i][j+x-1] == square[i+x-1][j] == square[i+x-1][j+x-1]:
                return True
            
    return False


n,m = map(int, input().split(' '))
square = []
res = []

# 직사각형 생성
for _ in range(n):
    square.append(input().rstrip())
    

num = min(n,m)
    
# 정사각형 찾기
## 제일 큰 정사각형부터 검사하기
for a in range(num, 0 ,-1):
    
    if find(a):
        print(a**2)
        break
        
    