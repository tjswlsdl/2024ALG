import sys
input = sys.stdin.readline
root = 0

N = int(input())
tree = [[]for _ in range(N+1)] # 2차원배열 tree 생성 여기에 자식넣을거임.
level = [0 for _ in range(N+1)] # 각 노드에 부여할 레벨넣을 리스트 생성

for i in range(1,N+1):
    num = int(input())
    
    if num == -1: # -1이면 root임.
        root = i
    else:         # -1아닌 num부모로 오고 그 노드는 노드i(자식) 임. 
        tree[num].append(i)

def dfs(r):
    for next in tree[r]: #r트리의 자식들이 next로 받아짐.
        level[next] = level[r]+1 #자식의 레벨 = 부모의 레벨+1
        dfs(next) # 자식도 dfs 호출

dfs(root)

for i in range(1,N+1):
    print(level[i])