
dx = [1,0,-1,0]
dy = [0, -1,0, 1]

arr = input()
cur_d = 3

pos_x, pos_y = 0, 0
for i in range(len(arr)):
    if arr[i] == 'L':
        cur_d = (cur_d - 1) % 4
    elif arr[i] == 'R':
        cur_d = (cur_d + 1) % 4 
    elif arr[i] == 'F':
        pos_x += dx[cur_d] 
        pos_y += dy[cur_d] 

print(pos_x, pos_y)