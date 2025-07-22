N, K = map(int, input().split())

arr = [0] * (N + 1)

for i in range(K):
    a, b = map(int, input().split())
    for j in range(a -1, b):
        arr[j] += 1 
   
max_v = 0
for i in range(N):
    if max_v < arr[i]:
        max_v = arr[i]

print(max_v)


