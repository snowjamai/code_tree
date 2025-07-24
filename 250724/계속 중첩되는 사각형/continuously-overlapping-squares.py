N = int(input())

board= [[0] * 201 for _ in range(201)]
color = 1

for i in range(N):
    x1,y1,x2, y2 = map(int, input().split())
    x1,y1,x2, y2 = x1+ 100,y1+ 100,x2+ 100, y2 + 100
    for h in range(y1,y2):
        for w in range(x1,x2):
            board[h][w] = color 

    if color == 1:
        color = 2
    elif color == 2:
        color = 1 


cnt = 0
for i in range(201):
    for j in range(201):
        if board[i][j] == 2:
            cnt += 1

print(cnt)