import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())


def dfs(start, visited, graph, group):
    # 현재 노드 그룹 저장
    visited[start] = group
    
    # 인접 노드 탐색
    for v in graph[start]:
        # 방문안한 노드
        if visited[v] == 0:
            result = dfs(v, visited, graph, -group)
            # -group : 현재 노드 그룹이랑 다른값 전달
            if not result:
                return False
            
        else:
            if visited[v] == group:
                return False
        
    return True


for _ in range(K):
    V, E = map(int, input().split(' '))

    # 각 정점에 근접한거 저장해야지
    graph = [[] for _ in range(V+1)]
    
    # 방문 여부 저장 리스트 ( 0:방문x / 1:집합A / -1:집합B )
    visited = [0] * (V+1)
    
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, V+1):
        if visited[i] == 0:
            result = (dfs(i, visited, graph, 1))
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")

    
    
    


