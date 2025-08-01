N, B = map(int, input().split())

arr = []
for i in range(N):
    a = int(input())
    arr.append(a)



max_cnt  = 0
for i in range(len(arr)):
    target_cost = arr[i] / 2 
    tmp = arr[:i] + arr[i + 1:] + [target_cost]
    tmp.sort()

    sum_v = 0
    cnt = 0

    for j in tmp:
        sum_v += j

        if sum_v > B: 
            break
        else:
            cnt += 1 
    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)


