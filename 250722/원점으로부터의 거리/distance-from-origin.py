N = int(input()) 

arr = []

num = 1
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y, num))
    num += 1

arr.sort(key=lambda x : (abs(x[0]) + abs(x[1]),x[2]))


for i in arr:
    print(i[2])