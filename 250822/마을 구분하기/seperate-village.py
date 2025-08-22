N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx, dy = [1,-1,0,0],[0,0,1,-1]
arr = {}

def dfs(x, y, v):
    global arr 

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue 
        else:
            if visited[ny][nx] == 0 and board[ny][nx] == 1:
                visited[ny][nx] = v
                arr[v] += 1
                dfs(nx, ny, v)
v = 1
for h in range(N):
    for w in range(N):
        if board[h][w] == 1 and visited[h][w] == 0:
            visited[h][w] = v 
            arr[v] = 1
            dfs(w,h,v)
            v += 1
tmp = [] 
for i in arr:
    tmp.append(arr[i])

tmp.sort(key = lambda x:x)

print(len(tmp))
for i in tmp:
    print(i)

    