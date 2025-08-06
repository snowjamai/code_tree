N, M =map(int, input().split())


board = [list(map(int, input().split())) for _ in range(N)]

def cnt_gold(x,y, k):
    cnt = 0
    for h in range(y - k, y + k + 1):
        for w in range(x - k, x + k + 1):
            if abs(w - x) + abs(h - y) > k:
                continue 
            else:
                if h < 0 or h >= N or w < 0 or w >= N:
                    continue 
                if board[h][w] == 1:
                    cnt += 1
    return cnt 

max_cnt = 0
max_cost = 0
for h in range(N):
    for w in range(N):
        for k in range(N):
            cnt = cnt_gold(w,h,k)
            cost = cnt * M 
            f_cost = cost - k * k - (k + 1) * (k + 1)
            # print(cnt, w, h, k, f_cost)
            if f_cost < 0:
                continue
            else:
                # print(cnt, f_cost)
                if max_cnt < cnt:
                    # max_cost = f_cost
                    max_cnt = cnt 

print(max_cnt) 


