N = int(input()) 
arr = []
num = 1
for i in range(N):
    w,h = map(int, input().split()) 
    arr.append((w,h,num))
    num += 1

arr.sort(key = lambda x: (x[0],-x[1]))

for i in arr:

    print(i[0], i[1], i[2])