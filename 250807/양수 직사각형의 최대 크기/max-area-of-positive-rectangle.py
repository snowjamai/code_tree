N , M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
max_s = -1

for h in range(N):
    for w in range(M):
        for hl in range(N ):
            for wl in range(M ):
                start_x, end_x = w, w + wl 
                start_y, end_y = h, h + hl 
                if start_x < 0 or start_x >= M or end_x < 0 or end_x >= M or start_y < 0 or start_y >= N or end_y < 0 or end_y >= N:
                    continue 
                else:
                    is_negative = False 
                    for i in range(start_y, end_y + 1):
                        for j in range(start_x, end_x + 1):
                            if board[i][j] <= 0 :
                                is_negative = True 
                                break
                        if is_negative == True:
                            break 
                    if is_negative == False:
                        s = (wl + 1) * (hl + 1) 
                        if s > max_s:
                            # print(start_x, start_y, end_x, end_y, wl, hl)
                            max_s =  s

print(max_s)