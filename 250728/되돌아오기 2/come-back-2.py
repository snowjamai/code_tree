commands = input()

# Please write your code here.
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

time = 1 
arr = [0] * 100001

cur_d = 3 
cx, cy = 0, 0
for i in commands:
    if i == 'F':
        nx, ny = cx + dx[cur_d], cy + dy[cur_d] 
        arr[time] = (nx, ny)
        cx, cy = nx, ny 
        time += 1 
    elif i == 'R': 
        arr[time] = (cx, cy)
        time += 1 
        cur_d = (cur_d + 1) % 4 
    elif i == 'L':
        arr[time] = (cx, cy)
        time += 1 
        cur_d = (cur_d - 1) % 4 

comp =  False 
for i in range(1, len(commands) + 1):
    if arr[i][0] == 0 and arr[i][1] == 0:
        comp = True 
        print(i)
        break

if comp == False:
    print("-1") 
    