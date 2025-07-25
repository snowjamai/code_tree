dx, dy = [1,-1,0,0],[0,0,1,-1]

N = int(input())

arr = [] 

for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


def check_rect(x, y):
    cnt = 0 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny <0 or ny >= N:
            continue 
        if arr[ny][nx] == 1:
            cnt += 1
    if cnt >= 3:
        return True 
    else:
        return False 
cnt = 0

for h in range(N):
    for w in range(N):
        if check_rect(w,h) == True:
            cnt += 1

print(cnt)
        