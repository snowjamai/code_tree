N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))
    
a, b = map(int, input().split())
c, d = map(int, input().split())


tmp = arr[:a -1] + arr[b:]
tmp = tmp[:c - 1] + tmp[d:]
print(len(tmp))
for i in tmp:
    print(i)
