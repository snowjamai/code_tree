N, K = map(int, input().split())

arr = [0] * 10001
for i in range(N):
    p, s = map(str, input().split())
    arr[int(p) - 1] = s 


def get_score(a):
    s = 0
    for i in range(a, a + K +1):
        if arr[i] == 'G':
            s += 1 
        elif arr[i] == 'H':
            s += 2

    return s 

max_s = 0
for i in range(len(arr) - K ):
    tmp = get_score(i)
    if max_s < tmp:
        max_s = tmp 
print(max_s)
