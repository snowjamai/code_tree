dx, dy = [1,-1, -1,1], [-1,-1, 1,1]

def get_num(x, y):
    start_x, start_y = x, y
    d = 0
    tmp = []
    tmp.append(board[y][x])

    while True:
        nx, ny = x + dx[d], y + dy[d] 
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            d += 1 
            if d >= 4:
                return -1
            nx, ny = x + dx[d], y + dy[d] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                return - 1
            else:
                if nx == start_x and ny == start_y:
                    return sum(tmp)
                
                tmp.append(board[ny][nx])
                x, y = nx, ny
        else:
            tmp.append(board[ny][nx])
            x, y = nx, ny 


            

            

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
max_v = 0

for h in range(N):
    for w in range(N):
        tmp = get_num(w, h)
        if max_v < tmp:
            max_v = tmp 
print(max_v)
