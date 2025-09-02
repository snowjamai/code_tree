N = int(input()) 

board = [list(map(int, input().split())) for _ in range(N)]


dp = [[0] * N for _ in range(N)]

for w in range(N):
    if w == 0:
        dp[0][w] = board[0][w]
    else:
        dp[0][w] =  dp[0][w - 1] + board[0][w]

for h in range(N):
    if h == 0:
        continue 
    else:
        dp[h][0] = dp[h - 1][0] + board[h][0]

for h in range(N):
    for w in range(N):
        if w == 0 or h == 0:
            continue 
        else:
            num1 = dp[h][w - 1]
            num2 = dp[h - 1][w]
            # print(num1, num2, w, h, board[h][w])
            if num1 < num2:
                dp[h][w] = num2 + board[h][w]
            else:
                dp[h][w] = num1 + board[h][w] 
print(dp[N -1][N - 1])
# for h in range(N):
#     for w in range(N):
#         print(dp[h][w], end = ' ')
#     print("")
