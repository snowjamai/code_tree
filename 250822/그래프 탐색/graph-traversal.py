N, M =map(int, input().split())

xy = []
graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    x, y = map(int,input().split())
    graph[y][x] = 1
    graph[x][y] = 1

    
visited = [0] * (N + 1) 

cnt = 0
def dfs(vertex):
    global cnt 
    for i in range(1, N + 1):
        if graph[vertex][i] == 1 and visited[i] == 0:
            visited[i] = 1 
            cnt += 1
            dfs(i)

visited[1] = 1
dfs(1)
print(cnt)
            

    
