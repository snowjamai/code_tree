board = [list(map(int, input().split())) for _ in range(4)]


d = input() 

def push_board(d):
    if d == 'L':
        for h in range(4):
            tmp = [] 
            for w in range(4):
                if board[h][w] != 0:
                    tmp.append(board[h][w])
            for i in range(4):
                if tmp == []:
                    board[h][i] = 0 
                else:
                    board[h][i] = tmp[0]
                    tmp = tmp[1:]
    elif d == 'R':
        for h in range(4):
            tmp = [] 
            for w in range(3, -1, -1):
                if board[h][w] != 0:
                    tmp.append(board[h][w])
            for i in range(3, -1, -1):
                if tmp == []:
                    board[h][i] = 0 
                else:
                    board[h][i] = tmp[0]
                    tmp = tmp[1:]
    elif d == 'U':
        for w in range(4):
            tmp = []
            for h in range(4):
                if board[h][w] != 0:
                    tmp.append(board[h][w])
            for i in range(4):
                if tmp == []:
                    board[i][w] = 0 
                else:
                    board[i][w] = tmp[0]
                    tmp = tmp[1:]
    elif d == 'D':
        for w in range(4):
            tmp = []
            for h in range(3, -1, -1):
                if board[h][w] != 0:
                    tmp.append(board[h][w])
            for i in range(3, -1, -1):
                if tmp == []:
                    board[i][w] = 0 
                else:
                    board[i][w] = tmp[0]
                    tmp = tmp[1:]


def print_board():
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=' ')
        print("")

def make_sum(d):
    if d == 'L':
        for h in range(4):
            for w in range(3):
                if board[h][w] == board[h][w + 1]:
                    board[h][w] = board[h][w] * 2
                    for i in range(w + 1, 3):
                        board[h][i] = board[h][i + 1]
                    board[h][3] = 0
    elif d == 'R':
        for h in range(4):
            for w in range(3, 0, -1):
                if board[h][w] == board[h][w - 1] and board[h][w] != 0:
                    board[h][w] = board[h][w] * 2
                    for i in range(w - 1, 0, -1):
                        board[h][i] = board[h][i - 1]
        
                    board[h][0] = 0
    elif d == 'U':
        for w in range(4):
            for h in range(3):
                if board[h][w] == board[h + 1][w]:
                    board[h][w] = 2 * board[h][w]
                    for i in range(h + 1, 3):
                        board[i][w] = board[i + 1][w]
                    board[3][w] = 0 
    elif d == 'D':
        for w in range(4):
            for h in range(3, 0, -1):
                if board[h][w] == board[h - 1][w]:
                    board[h][w] = 2 * board[h][w]
                    for i in range(h - 1, 0, -1):
                        board[i][w] = board[i - 1][w]
                    board[0][w] = 0

push_board(d)
make_sum(d)
print_board()