N = int(input())
arr = []
for i in range(N):
    a, b, c = map(int, input().split())

    arr.append((a, b, c))

def simul(idx):
    if idx == 0:
        tmp = [1,0,0]
    elif idx == 1:
        tmp = [0,1,0]
    elif idx == 2:
        tmp = [0, 0, 1]

    score = 0 
    for i in arr:
        tmp_v = tmp[i[0] - 1]
        tmp[i[0] - 1] = tmp[i[1] - 1]
        tmp[i[1] - 1] = tmp_v 
        if tmp[i[2] - 1] == 1:
            score += 1

    return score 

max_cnt = 0
for i in range(3):
    cnt = simul(i)

    if cnt > max_cnt:
        max_cnt = cnt 

print(max_cnt)