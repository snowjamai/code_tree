N = int(input())

arr = []

for i in range(N):
    x, y = map(int,input().split())
    arr.append((x,y))

min_d = float('inf')

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            d = (arr[i][0] - arr[j][0])*(arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1])*(arr[i][1] - arr[j][1])
            if d < min_d:
                min_d = d 

print(min_d)