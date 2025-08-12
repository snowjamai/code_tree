

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def is_fit(x, y):
    for i in range(M):
        if board[y][x + i] != 0:
            return False
    return True 

def fill(x, y):
    for i in range(M):
        board[y][x + i] = 1

fit_comp = False 

for h in range(N -1, -1, -1):
    for w in range(N - M + 1):
        if is_fit(w, h) == True:
            fit_comp = True 
            fill(w, h)
            break 

    if fit_comp == True:
        break 


for h in range(N):
    for w in range(N):
        print(board[h][w], end = ' ')
    print("")
