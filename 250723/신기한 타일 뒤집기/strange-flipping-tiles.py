arr = [0] * 200001

N = int(input())

base_p = 100000
for i in range(N):
    a, b =map(str, input().split())
    if b == 'L':
        tar_p = base_p - int(a) + 1
        for j in range(tar_p, base_p + 1):
            arr[j] = 1 
        base_p = tar_p
    if b == 'R':
        tar_p = base_p + int(a) - 1
        for j in range(base_p, tar_p + 1):
            arr[j] = 2 
        base_p = tar_p

bl_cnt = 0
wh_cnt = 0
for i in range(200001):
    if arr[i] == 1:
        wh_cnt += 1
    elif arr[i] == 2:
        bl_cnt += 1
print(wh_cnt, bl_cnt)

