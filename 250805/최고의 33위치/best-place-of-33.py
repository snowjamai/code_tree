def get_coin(x, y):
    cnt = 0
    for h in range(y, y + 3):
        for w in range(x, x + 3):
            if board[h][w] == 1:
                cnt += 1

    return cnt 


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
for i in range(N - 2):
    for j in range(N - 2):
        cnt = get_coin(j,i)

        if cnt > max_cnt:
            max_cnt = cnt 

print(max_cnt)
