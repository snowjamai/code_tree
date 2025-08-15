N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

bomb = [] 
for h in range(N):
    for w in range(N):
        if board[h][w] == 1:
            bomb.append((w, h))
max_cnt = 0

def dfs(cnt, bomb_size):
    global max_cnt

    if cnt == len(bomb):
        empty = [[0] * N for _ in range(N)]

        for i in range(len(bomb)):
            bx, by = bomb[i][0], bomb[i][1] 
            bs = bomb_size[i]
            if bs == 0:
                dx, dy = [0,0],[-1,1]
                for j in range(3):
                    for k in range(2):
                        nx, ny = bx + dx[k] * j, by + dy[k] * j 
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue 
                        else:
                            empty[ny][nx] = 1
            elif bs == 1:
                dx, dy = [1,0,-1,0], [0,1,0,-1]
                for j in range(2):
                    for k in range(4):
                        nx, ny = bx + dx[k] * j, by + dy[k] * j 
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue 
                        else:
                            empty[ny][nx] = 1
            elif bs == 2:
                dx, dy = [-1, 1, 1, -1], [-1,-1,1,1]
                for j in range(2):
                    for k in range(4):
                        nx, ny = bx + dx[k] * j , by + dy[k] * j 
                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue 
                        else:
                            empty[ny][nx] = 1
        cnt = 0 
        for h in range(N):
            for w in range(N):
                if empty[h][w] == 1:
                    cnt += 1 
        if max_cnt < cnt:
            max_cnt = cnt 
    else:
        for i in range(3):
            bomb_size.append(i)
            dfs(cnt + 1, bomb_size)
            bomb_size.pop()


dfs(0, [])
print(max_cnt)
                    
                

