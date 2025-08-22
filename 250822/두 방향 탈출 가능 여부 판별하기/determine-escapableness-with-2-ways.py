N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

s_x,s_y = 0,0
e_x, e_y = M - 1, N - 1

dx, dy = [1,0], [0,1]

visited = [[0] * M for _ in range(N)]
is_goal = False
def dfs(x, y):
    global is_goal
    if x == e_x and y == e_y:
        is_goal = True 
        return

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue 
        else:
            if visited[ny][nx] == 0 and board[ny][nx] == 1:
                visited[ny][nx] = 1
                dfs(nx, ny)
                # visited[ny][nx] = 0 
    
dfs(0, 0)
if is_goal == True:
    print("1")
else:
    print("0")


        
