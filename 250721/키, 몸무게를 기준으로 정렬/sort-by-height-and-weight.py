N = int(input())

arr = [] 
for i in range(N):
    name, h, w = map(str, input().split())
    arr.append((name,int(h),int(w)))

arr.sort(key=lambda x: (x[1],-x[2]))

for i in arr:
    print(i[0], i[1], i[2])
