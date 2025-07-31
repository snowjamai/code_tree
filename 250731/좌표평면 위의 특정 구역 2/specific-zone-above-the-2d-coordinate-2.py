N = int(input())

arr = [] 
for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
    
def get_s(arr):
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -float('inf'), -float('inf')
    
    for i in arr:
        if min_x > i[0]:
            min_x = i[0]
        if max_x < i[0]:
            max_x = i[0] 
        if min_y  > i[1]:
            min_y = i[1]
        if max_y < i[1]:
            max_y = i[1] 

    return((max_y - min_y) * (max_x - min_x))

min_s = -1

for i in range(len(arr)):
    tmp = arr[:i] + arr[i + 1:]
    s = get_s(tmp)
    if min_s == -1:
        min_s = s 
    if s < min_s:
        min_s = s 

if min_s == -1:
    print("0")
else:
    print(min_s)
