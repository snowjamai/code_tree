n = int(input())

arr = []
num = 1
for i in range(n):
    h, w = map(int, input().split())
    arr.append((h,w, num))
    num += 1

arr.sort(key=lambda x:(-x[0],-x[1],x[2]))
for i in arr:
    print(i[0], i[1], i[2])