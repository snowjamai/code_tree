N, K = map(int, input().split())

arr = [0] * 101 

for i in range(N):
    a, b = map(int, input().split())

    arr[b] = a


max_v = 0
for i in range(K, 101- K ):
    tmp = arr[i - K:i + K + 1]

    sum_v = sum(tmp)
    if max_v < sum_v:
       
        max_v = sum_v

print(max_v)
