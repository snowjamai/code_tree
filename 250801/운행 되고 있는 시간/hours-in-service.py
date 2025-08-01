N = int(input())

arr = []
for i in range(N):
    a,b = map(int, input().split())

    arr.append((a, b)) 

def get_time(arr):
    time = [0] * 1001 
    for i in arr:
        for j in range(i[0],i[1]):
            time[j] = 1
    cnt = 0
    for i in range(1,1001):
        if time[i] == 1:
            cnt += 1

    return cnt 

max_t = 0

for i in range(len(arr)):
    tmp = arr[:i] + arr[i+1:]
    t = get_time(tmp)
    if max_t < t:
        max_t = t
print(max_t)
