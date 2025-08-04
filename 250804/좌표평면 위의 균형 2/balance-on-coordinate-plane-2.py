N = int(input())

arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))



def get_cnt(x, y):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    
    for i in arr:
        if i[0] > x and i[1] > y:
            cnt1 += 1
        elif i[0] > x and i[1] < y:
            cnt4 += 1
        elif i[0] < x and i[1] > y:
            cnt2 += 1
        elif i[0] < x and i[1] < y:
            cnt3 += 1 
    max_cnt = 0
    if max_cnt < cnt1:
        max_cnt = cnt1 
    if max_cnt < cnt2:
        max_cnt = cnt2
    if max_cnt < cnt3:
        max_cnt = cnt3
    if max_cnt < cnt4:
        max_cnt = cnt4 
    return max_cnt 

min_cnt = float('inf')
for i in range(2, 99):
    if i % 2 != 0:
        continue 
    else:
        for j in range(2, 99):
            if j % 2 != 0:
                continue 
            else:
                cnt = get_cnt(i, j)

                if cnt < min_cnt:
                    min_cnt = cnt 

print(min_cnt)
                

