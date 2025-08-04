board = [list(map(int, input())) for _ in range(3)]

dx, dy = [1,0,1,1], [0,1,1,-1] 

cnt = 0
tmp = {}

for h in range(3):
    for w in range(3):
        for i in range(4):
            lw = w + dx[i] * 2 
            lh = h + dy[i] * 2

            if lw < 0 or lw >= 3 or lh < 0 or lh >=3:
                continue 
            else:
                first = board[h][w]
                second = board[h + dy[i]][w + dx[i]]
                third = board[h + dy[i] * 2][w + dx[i] * 2]
                if first == second and first != third or first == third and first != second or second == third and first != second:
                    arr = [first, second, third]
                    arr.sort() 
                    if (arr[0], arr[-1]) not in tmp:
                        tmp[(arr[0], arr[-1])] = 1 
                    
                        cnt += 1

print(cnt)