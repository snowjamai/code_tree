dx, dy = [1,-1, 0,0],[0,0,1,-1]

N = int(input())
arr = [0] * 1001
t = 0 

x, y= 0 , 0
for i in range(N):
    d, k = map(str, input().split())
    if d == 'N':
        for j in range(t + 1, t + 1 + int(k)):
            nx = x + dx[2] 
            ny = y + dy[2] 
            arr[j]=(nx, ny)
            x, y = nx, ny 
        t += int(k)
    elif d == 'E':
        for j in range(t + 1, t + 1 + int(k)):
            nx = x + dx[0] 
            ny = y + dy[0] 
            arr[j]=(nx, ny)
            x, y = nx, ny 
        t += int(k)
    elif d == 'W':
        for j in range(t + 1, t + 1 + int(k)):
            nx = x + dx[1] 
            ny = y + dy[1] 
            arr[j]=(nx, ny)
            x, y = nx, ny 
        t += int(k)
    elif d == 'S':
        for j in range(t + 1, t + 1 + int(k)):
            nx = x + dx[3] 
            ny = y + dy[3] 
            arr[j]=(nx, ny)
            x, y = nx, ny 

        t += int(k)
check  =False
for i in range(t + 1):
    if arr[i] == 0:
        continue
    else:
        if arr[i][0] == 0 and arr[i][1] == 0:
            check = True 
            print(i)
            break

if check == False:
    print("-1")

    