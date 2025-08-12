import copy


def find_match(arr):
    tmp = []
    dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
    
    for h in range(N):
        for w in range(N):
            for i in range(4):
                nx, ny = w + dx[i], h + dy[i] 
                if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[ny][nx] == 0:
                    continue
                else:
                    if arr[ny][nx] == arr[h][w]:
                        m = [(nx,ny), (w, h)]
                        m.sort(key = lambda x: (x[0],x[1]))
                        if m not in tmp:
                            tmp.append(m)

    return tmp 


def bomb(x, y):
    b_s = board[y][x] 
    tmp = copy.deepcopy(board) 

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    for i in range(b_s):
        for j in range(4):
            nx, ny = x + dx[j] * i, y + dy[j]*i
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            else:
                tmp[ny][nx] = 0

    return tmp
def get_down(arr):
    for w in range(N):
        tmp = [] 
        for h in range(N - 1, -1, -1):
            if arr[h][w] != 0:
                tmp.append(arr[h][w])
        for h in range(N - 1, -1, -1):
            if tmp == []:
                arr[h][w] = 0
            else:
                arr[h][w] = tmp[0]
                tmp = tmp[1:]
    return arr 
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_len = 0
for h in range(N):
    for w in range(N):
        tmp_board = bomb(w, h)
        tmp_board = get_down(tmp_board)
        a = find_match(tmp_board)
        len_a = len(a)
        if max_len < len_a:
            max_len = len_a
            b = a

print(max_len)
