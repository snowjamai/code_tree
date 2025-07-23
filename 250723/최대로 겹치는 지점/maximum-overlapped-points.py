N = int(input())

arr = [0] * 101

for i in range(N):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        arr[j] += 1

max_v = 0 
for i in range(101):
    if max_v  < arr[i]:
        max_v = arr[i]

print(max_v)

    