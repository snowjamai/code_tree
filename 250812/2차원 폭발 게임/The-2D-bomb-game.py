N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def find_column_bomb(x):
    cnt = 1 
    bs = 0

    for h in range(N):
        if h == 0:
            continue 
        else:
            if board[h][x] != board[h - 1][x]:
                if cnt >= M:
                    for i in range(bs, h):
                        board[i][x] = 0 
                bs = h 
                cnt = 1
            else:
                cnt += 1

    if cnt >= M:
        for i in range(bs,N):
            board[i][x] = 0
    
    
def print_board():
    for h in range(N):
        for w in range(N):
            print(board[h][w], end = ' ')
        print("") 

def rotate():
    tmp = [[0] * N for _ in range(N)] 
    for h in range(N):
        for w in range(N):
            x, y= w, h
            cx, cy = N - 1 - y, x 
            tmp[cy][cx] = board[y][x]
    return tmp 

def make_d(x):
    tmp = [] 
    for i in range(N):
        if board[i][x] != 0:
            tmp.append(board[i][x]) 

    for i in range(N-1, -1, -1):
        if tmp == []:
            board[i][x] = 0 
        else:
            board[i][x] = tmp[-1]
            tmp = tmp[:-1] 

def find_bomb():
    for i in range(N):
        find_column_bomb(i)
        
def is_bomb():
    for w in range(N):
        cnt = 1
        for h in range(N):
            if h == 0:
                continue 
            else:
                if board[h][w] != 0:
                    if board[h][w] != board[h - 1][w]:
                        if cnt >= M:
                            return True 
                    else:
                        cnt += 1
                
        if cnt >= M:
            return True 
    return False 


for i in range(K):
    while is_bomb():
        find_bomb()
        for i in range(N):
            make_d(i)
            
    board= rotate()
    for i in range(N):
        make_d(i)
    # print_board()

while is_bomb():
    find_bomb()
    for i in range(N):
        make_d(i)
    
cnt = 0
for h in range(N):
    for w in range(N):
        if board[h][w] != 0:
            cnt += 1

print(cnt)
