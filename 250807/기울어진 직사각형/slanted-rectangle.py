dx, dy = [1,-1, -1,1], [-1,-1, 1,1]


max_v = 0

def get_num(x, y, d, sum_v, first_x, first_y):
    global max_v
    if x < 0 or x >= N or y < 0 or y >= N or d >= 4:
        return 
    else:
        nx, ny = x + dx[d], y + dy[d] 
        if nx == first_x and ny == first_y:
            sum_v += board[y][x]
            if sum_v > max_v:
                max_v = sum_v
        tmp = sum_v + board[y][x] 
        get_num(nx, ny, d, tmp, first_x, first_y)
        get_num(nx, ny, d + 1, tmp, first_x, first_y)
            

    
        


    
    

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

for h in range(N):
    for w in range(N):
        get_num(w, h, 0 , 0 , w, h)
        
print(max_v)
