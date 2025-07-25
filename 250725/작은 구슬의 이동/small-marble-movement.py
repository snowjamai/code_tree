N, T = map(int, input().split())
R, C, D= map(str, input().split())
R, C = int(R), int(C)

dx, dy = [1, 0 , - 1, 0],  [0, 1, 0, -1]

if D == 'U':
    d = 3
elif D == 'D':
    d = 1
elif D == 'R':
    d = 0
elif D == 'L':
    d = 2
cx, cy = C, R 

for i in range(T):
    nx, ny = dx[d] + cx, dy[d] + cy 
    if nx <= 0 or ny <= 0 or nx > N or ny > N:
        d = (d + 2) % 4 
        nx, ny = cx, cy
        # nx, ny = dx[d] + cx, dy[d] + cy 
    cx, cy = nx, ny 

print(cy, cx)
        