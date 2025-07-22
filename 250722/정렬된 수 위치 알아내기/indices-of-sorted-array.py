N = int(input()) 

arr = list(map(int, input().split()))

arr2 = []

num = 1
for i in arr:
    arr2.append((i, num))
    num += 1 

arr2.sort(key=lambda x: (x[0], x[1]))

re = [0] * (N + 1) 
for i in range(len(arr2)):
    re[arr2[i][1]] = i + 1

for i in range(1, N + 1):
    print(re[i], end=' ')