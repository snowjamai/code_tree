N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [1,-1,0,0],[0,0,1,-1]
bomb = [] 
def is_bomb(x, y, cnt):
    global bomb, visited

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] 
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue 
        if board[ny][nx] == board[y][x] and visited[ny][nx] == 0 and board[ny][nx] != 0:
            visited[ny][nx] = 1 
            bomb.append((nx, ny))
            is_bomb(nx, ny, cnt + 1)

max_v = 0
cnt = 0
for h in range(N):
    for w in range(N):
        visited = [[0] * N for _ in range(N)]
        bomb = [(w, h)] 
        visited[h][w] = 1
        is_bomb(w,h,1)
        len_b = len(bomb)
        if len_b > max_v:
            max_v = len_b 

        if len_b >= 4:
            cnt += 1
            for i in bomb:
                board[i[1]][i[0]] = 0 
            

print(cnt, max_v)



        


    