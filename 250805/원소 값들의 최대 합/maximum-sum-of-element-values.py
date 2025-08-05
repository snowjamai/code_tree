N, M = map(int, input().split())



arr = list(map(int, input().split()))
max_v = 0
for c in range(N):
    select = c - 1
    sum_v = 0
    for i in range(M):
        num = arr[select] - 1
        sum_v += num + 1
        select = num 
    if max_v < sum_v:
        max_v = sum_v

print(max_v)
