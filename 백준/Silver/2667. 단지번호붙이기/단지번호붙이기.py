import sys
input = sys.stdin.readline

T = int(input())
res = []

#전체지도
maps = []

#지도생성
for _ in range(T):
    maps.append(list(map(int, input().rstrip())))

#print(maps)    
'''
입력받은걸 어떻게 근접 판단하지,, 양옆위아래 인덱스를 따지도록 돌려야하나 ㅜ
인덱스 확인할때 계속 오른쪽이랑 아래만확인하면될듯?
왜냐면 전거에서 체크한건 또할필요없으니깐
'''
#x, y 축 이동 리스트
xx = [0, 0, 1, -1]
yy = [1,-1, 0,  0]


cnt = 0


def counting(x,y):
    global cnt
    # idx 범위 지도 안쪽 제한
    if x<0 or x>=T or y<0 or y>=T:
        return
    
    if maps[x][y] == 1:
        cnt += 1
        maps[x][y] = 0
        
        for i in range(4):
            loc_x = x + xx[i]
            loc_y = y + yy[i]
            counting(loc_x,loc_y)
            
for i in range(T):
    for j in range(T):
        if maps[i][j]==1:
            counting(i,j)
            res.append(cnt)
            cnt = 0

res.sort()   
    

# 결과 출력
print(len(res))
for num in res:
    print(num)





