N = int(input())
grid = [list(input()) for _ in range(N)]
K = int(input())

# Please write your code here.


dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

cnt = 0


if K <= N:
    cd = 1 
    pos_x, pos_y = K - 1, 0 
elif K <= 2 * N:
    cd = 2 
    pos_x, pos_y = N - 1, K - N - 1
elif K <= 3 * N:
    cd = 3 
    pos_x, pos_y = N * N - K, N - 1 
elif K <= 4 * N:
    cd = 0
    pos_x, pos_y = 0, 4 * N - K 


# / 뱡향일때 
# d = 0 -> nd = 3 
# d = 1 -> nd = 2
# d = 2 -> nd = 1
# d = 3 -> nd = 0

# \ 방향일때
# d = 0 -> nd = 1
# d = 1 -> nd = 0
# d = 2 -> nd = 3
# d = 3 -> nd = 2 

while True: 
    print(pos_x, pos_y, cd)
    if grid[pos_y][pos_x] == '/':
        if cd == 0:
            nd = 3
        elif cd == 1:
            nd = 2
        elif cd == 2:
            nd = 1
        elif cd == 3:
            nd = 0
        nx, ny = pos_x + dx[nd], pos_y + dy[nd] 
        cd = nd 
        cnt += 1 
    elif grid[pos_y][pos_x] == '\\':
        if cd == 0:
            nd = 1
        elif cd == 1:
            nd = 0
        elif cd == 2:
            nd = 3
        elif cd == 3:
            nd = 2 
        nx, ny = pos_x + dx[nd], pos_y + dy[nd] 
        cd = nd 
        cnt += 1 
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break 
    pos_x, pos_y= nx, ny
print(cnt)