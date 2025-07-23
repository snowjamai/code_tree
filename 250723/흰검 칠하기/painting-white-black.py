black_arr = [0] * 200001
white_arr = [0] * 200001
cur_arr = [0] * 200001

N = int(input())
base_pos = 100000

for i in range(N):
    a, b = map(str, input().split()) 

    if b == 'L':
        target_pos = base_pos - int(a) 
        for j in range(target_pos, base_pos):
            white_arr[j] += 1
            if black_arr[j] >= 2 and white_arr[j] >= 2:
                cur_arr[j] = 3 
            else:
                cur_arr[j] = 1 
        base_pos = target_pos

    elif b == 'R':
        target_pos = base_pos + int(a)

        for j in range(base_pos, target_pos):
            black_arr[j] += 1 
            if black_arr[j] >= 2 and white_arr[j] >= 2:
                cur_arr[j] = 3
            else:
                cur_arr[j] = 2 

        base_pos = target_pos
    
black_cnt = 0
white_cnt = 0
gray_cnt = 0

for i in range(200001):
    if cur_arr[i] == 1:
        white_cnt += 1
    elif cur_arr[i] == 2:
        black_cnt += 1
    elif cur_arr[i] == 3:
        gray_cnt += 1

print(white_cnt, black_cnt, gray_cnt)



        

