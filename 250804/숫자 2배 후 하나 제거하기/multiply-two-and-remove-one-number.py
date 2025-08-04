N = int(input())

arr = list(map(int, input ().split()))
min_sub = float('inf')
for i in range(N):
    arr[i] = arr[i] * 2
    for j in range(N):
        if i == j:
            continue 
        else:
            tmp = arr[:j] + arr[j + 1:]
            sum_sub = 0
            for k in range(len(tmp) - 1):
                sub = abs(tmp[k + 1] - tmp[k])
                sum_sub += sub 
            if sum_sub < min_sub:
                min_sub = sum_sub
    arr[i] = arr[i] // 2
print(min_sub)