N = int(input())

arr = [] 
max_h = 0
for i in range(N):
    h = int(input())
    if max_h < h:
        max_h = h 
    arr.append(h)


def get_cnt(del_h):
    tmp = []
    for i in range(len(arr)):
        if arr[i] - del_h <= 0:
            tmp.append(0)
        else:
            tmp.append(1)
    cnt = 0
    for i in range(len(tmp) - 1):
        if tmp[i] == 1 and tmp[i + 1] == 0:
            cnt += 1
    if tmp[-2] == 0 and tmp[-1] == 1:
        cnt += 1 
    elif tmp[-2] == 1 and tmp[-1] == 1:
        cnt += 1 

    return cnt 


cnt_max = 0
for i in range(1, max_h):
    tmp = get_cnt(i)
    if tmp > cnt_max:
        cnt_max = tmp 

print(cnt_max)



    