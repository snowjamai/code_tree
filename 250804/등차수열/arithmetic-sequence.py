N = int(input())


arr = list(map(int, input().split()))

max_cnt = 0
for k in range(1, 101):
    cnt = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if arr[j] - k == k - arr[i]:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt 

print(max_cnt)