

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
def pull(x, y):
    for i in range(M):
        board[y][x + i] = 0 

fit_comp = False 
for h in range(N):
    if is_fit(K - 1, h) == True and fit_comp == False:
        fit_comp = True 
        fill(K - 1, h)
    elif is_fit(K - 1, h) == True and fit_comp == True:
        pull(K - 1, h - 1) 
        fill(K - 1, h) 
    elif  is_fit(K - 1, h) == False and fit_comp == True:
        break 
    

       



for h in range(N):
    for w in range(N):
        print(board[h][w], end = ' ')
    print("")
