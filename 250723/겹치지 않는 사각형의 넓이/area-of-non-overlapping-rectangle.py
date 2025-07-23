ax1, ay1, ax2, ay2 = map(int, input().split()) 
bx1, by1, bx2, by2 = map(int, input().split()) 
Mx1, My1, Mx2, My2 = map(int, input().split()) 

board = [[0]* 2001 for _ in range(2001)]
ax1, ay1, ax2, ay2 = ax1 + 1000, ay1 + 1000, ax2 + 1000, ay2 + 1000

bx1, by1, bx2, by2 = bx1 + 1000, by1 + 1000, bx2 + 1000, by2 + 1000
Mx1, My1, Mx2, My2 = Mx1 + 1000, My1 + 1000, Mx2 + 1000, My2 + 1000
for i in range(ay1, ay2):
    for j in range(ax1, ax2):
        board[i][j] = 1 


for i in range(by1, by2):
    for j in range(bx1, bx2):
        board[i][j] = 1 

for i in range(My1, My2):
    for j in range(Mx1, Mx2):
        if board[i][j] == 1:
            board[i][j] = 0

tot = 0
for i in range(2001):
    for j in range(2001):
        if board[i][j] == 1:
            tot += 1

print(tot)
        