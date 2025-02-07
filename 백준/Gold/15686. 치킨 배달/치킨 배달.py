import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

mat = []

for _ in range(n):
    mat.append(list(map(int, input().split(' '))))
    
# print(mat)
    
# 치킨 집 좌표, 집 좌표 저장하는 리스트 만들어서 각 집에 대한 치킨 거리를 구하자
chick = []
house = []

for x in range(n):
    for y in range(n):
        if mat[x][y] == 1:
            house.append((x,y))
        elif mat[x][y] == 2:
            chick.append((x,y))


# 2차원 배열 백트래킹 코드 공식
arr = []           
real_check = int(1e9)
def back(num, cnt) :
    global real_check
    # 치킨 리스트에 담은 좌표들이 개수보다 커지면 인덱스에러나서 방지해주는 것
    if num > len(chick):
        return
    # cnt 는 최대 몇개의 좌표를 뽑을지 보는 것이라서 cnt == m 이 되면 좌표쌍을 뽑기 시작함.
    if cnt == m:
        res_total = 0
        for hx, hy in house:
            min_check = int(1e9)
            for idx in arr:
                cx, cy = chick[idx]
                min_check = min(min_check, abs(hx-cx)+abs(hy-cy))
                
            res_total += min_check
            
        real_check = min(res_total, real_check)
        return
    
    arr.append(num)
    back(num+1, cnt+1)
    arr.pop()
    back(num+1, cnt)
    return real_check
    
print((back(0,0)))
    
