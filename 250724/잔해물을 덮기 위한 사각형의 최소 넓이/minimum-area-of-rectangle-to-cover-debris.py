board = [[0] * 2001 for _ in range(2001)]


x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+ 1000, y1+ 1000, x2+ 1000, y2 + 1000

for i in range(y1, y2):
    for j in range(x1, x2):
        board[i][j] = 1


x3, y3, x4, y4 = map(int, input().split())
x3, y3, x4, y4 = x3+ 1000, y3+ 1000, x4+ 1000, y4 + 1000


for i in range(y3, y4):
    for j in range(x3, x4):
        board[i][j] = 0



min_x = 2001
max_x = -1
min_y = 2001
max_y = -1

for i in range(y1, y2):
    for j in range(x1, x2):
        if board[i][j] == 1:
            if j < min_x:
                min_x = j
            if j > max_x:
                max_x = j 
            
            if i < min_y:
                min_y = i 
            if i > max_y:
                max_y = i 
if max_y == -1:
    print("0")
else:
    print((max_y - min_y + 1) * (max_x - min_x + 1))