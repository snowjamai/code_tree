N, M = map(int, input().split())


# Please write your code here.


dx, dy = [1,-1,0,0], [0,0,1,-1]

def is_patient(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        else:
            if board[ny][nx] == 1:
                cnt += 1 
    if cnt == 3:
        return True 
    else:
        return False 


board = [[0] * N for _ in range(N)]



for i in range(M):
    r, c = map(int, input().split())

    board[r - 1][c - 1] = 1
    if is_patient(c - 1, r - 1) == True:
        print("1")
    else:
        print("0")