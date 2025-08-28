from collections import deque

dx, dy = [1,-1,0,0], [0,0,1,-1]

N, K, U, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def select(l, idx):
    if len(l) == K:
        print(l)
        return 
    else:
        for i in range(idx, N):
            l.append(i)
            select(l, i + 1)
            l.pop()

select([], 0)

a = deque()
a.append(1)
a.append(2)
a.popright()
print(a)