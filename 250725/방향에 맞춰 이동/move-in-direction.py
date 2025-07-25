N = int(input())
dx, dy = [1,-1,0,0], [0,0,-1,1]

# 0 -> E
# 1 -> W
# 2 -> S
# 3 -> N


pos_x, pos_y = 0, 0
for i in range(N):
    d, x = map(str, input().split())
    if d == 'E':
        pos_x += dx[0]*int(x)
        pos_y += dy[0]*int(x)
    elif d == 'W':
        pos_x += dx[1]*int(x)
        pos_y += dy[1]*int(x)
    elif d == 'S':
        pos_x += dx[2]*int(x)
        pos_y += dy[2]*int(x)
    elif d == 'N':
        pos_x += dx[3]*int(x)
        pos_y += dy[3]*int(x)



print(pos_x, pos_y)