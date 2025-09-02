N = int(input()) 

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]* N for _ in range(N)]

for h in range(N - 1, -1, -1):
    if h == N - 1:
        dp[0][h] = board[0][h]
    else:
        dp[0][h] = dp[0][h + 1] + board[0][h]

for h in range(N):
    if h == 0:
        continue 
    else:
        dp[h][N - 1] = dp[h - 1][N - 1] + board[h][N - 1]

for h in range(1, N):
    for w in range(N - 2, -1, -1):
        num1 = dp[h - 1][w]
        num2 = dp[h][w + 1]
        if num1 < num2:
            dp[h][w] = num1 + board[h][w] 
        else:
            dp[h][w] = num2 + board[h][w] 

print(dp[N- 1][0])
