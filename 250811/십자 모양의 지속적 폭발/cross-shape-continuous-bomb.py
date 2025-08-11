N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

arr = [] 
for i in range(M):
    c = int(input())
    arr.append(c - 1)


def bomb_simul(x):
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    for h in range(N):
        if board[h][x] != 0:
            b_len = board[h][x]
            for i in range(b_len):
                for j in range(4):
                    nx, ny = x + dx[j]*i , h + dy[j] * i 
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue 
                    else:
                        board[ny][nx] = 0 


    
    
def down_board(x):
    tmp = [] 
    for i in range(N):
        if board[i][x] != 0:
            tmp.append(board[i][x])

    for i in range(N - 1, -1, -1):
        if tmp == []:
            board[i][x] = 0
        else:
            board[i][x] = tmp[-1]
            tmp = tmp[:-1]
     
    

                


for i in arr:
    bomb_simul(i)
    for i in range(N):
        down_board(i) 

for h in range(N):
    for w in range(N):
        print(board[h][w], end = ' ')
    print("")