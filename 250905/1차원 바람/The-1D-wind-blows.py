N, M , Q = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

arr = []
for i in range(Q):
    r, d = map(str, input().split())
    arr.append((int(r) - 1, d))

def match_cehck(r, d):
    if d == 'U':
        for w in range(M):
            if board[r-1][w] == board[r][w]:
                return True
    elif d == 'D':
        for w in range(M):
            if board[r+1][w] == board[r][w]:
                return True 
    return False 
            
def shift(r, d):
    if d == 'R':
        board[r][:] = board[r][1:] + board[r][:1]
    elif d == 'L':
        board[r][:] = board[r][-1:] + board[r][:-1]
        
def simul(r, d):
    shift(r, d)

    target_r = r 
    target_d = d 
    if target_r > 0:
        while match_cehck(target_r, 'U'):
            if target_d == 'L':
                target_d = 'R'
            else:
                target_d = 'L' 

            target_r -= 1 
            shift(target_r, target_d)
            if target_r == 0:
                break
    
    target_r = r 
    target_d = d 
    if target_r < N - 1 :
        while match_cehck(target_r, 'D'):
            if target_d == 'L':
                target_d = 'R'
            else:
                target_d = 'L' 
            target_r += 1 
            shift(target_r, target_d)
            if target_r == N - 1:
                break
        

def print_board():
    for h in range(N):
        for w in range(M):
            print(board[h][w], end = ' ')
        print("")

for i in range(len(arr)):
    simul(arr[i][0], arr[i][1])

print_board()