board = [[0] * 201 for _ in range(201)]

N = int(input())

for i in range(N):
    a, b = map(int, input().split()) 
    a, b = int(a) + 100, int(b) + 100
    for i in range(b, b + 8):
        for j in range(a, a + 8):
            board[i][j] = 1 
        

tot = 0
for h in range(201):
    for w in range(201):
        if board[h][w] == 1:
            tot += 1

print(tot)
            
