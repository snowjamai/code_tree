
from collections import deque 
import copy 
class queue:
    def __init__(self):
        self.q = deque() 
    def push(self, v):
        self.q.append(v)
    def pop(self):
        return self.q.popleft()
        
    def empty(self):
        if len(self.q) == 0:
            return True 
        return False 
    def front(self):
        return self.q[0]

        
N, K, M =map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
q = queue()
rock = [] 

for h in range(N):
    for w in range(N):
        if board[h][w] == 1:
            rock.append((w, h))


for i in range(K):
    r,c = map(int, input().split())
    q.push((c - 1, r - 1))
max_cnt = 0

def dfs(l, idx, cnt):
    global max_cnt
    if cnt > M:
        a = bfs(l, q)
        if (a - 1) > max_cnt:
            max_cnt = (a - 1)
        return 
    for i in range(idx, len(rock)):
        l.append(i)
        dfs(l,i + 1,cnt + 1)
        l.pop() 

    

def bfs(l, q):
    tmp = copy.deepcopy(q)
    tmp_board = copy.deepcopy(board)
    visited = [[0]* N for _ in range(N)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    fx, fy = tmp.front() 
    visited[fy][fx] = 1
    cnt = 0
    for i in l:
        tmp_board[rock[i][1]][rock[i][0]] = 0 

    while tmp.empty() == False:
        x, y = tmp.pop() 
        cnt  += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if tmp_board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1 
                tmp.push((nx, ny)) 
            
    return cnt




dfs([],0,1)

print(max_cnt)

    