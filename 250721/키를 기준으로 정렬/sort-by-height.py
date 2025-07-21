N = int(input()) 

arr = []
for i in range(N):
    a, b, c = map(str, input().split()) 
    arr.append((a, int(b), int(c)))


arr.sort(key = lambda x:x[1])

for i in arr:
    print(i[0], i[1], i[2])
