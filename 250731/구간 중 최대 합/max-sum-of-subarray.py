N, K = map(int ,input().split())

arr = list(map(int, input().split()))

def get_sum(a):
    s = 0
    for i in range(a, a + K):
        s += arr[i]

    return s 

max_sum = 0
for i in range(len(arr) - K):
    s = get_sum(i)

    if s > max_sum:
        max_sum = s 

print(max_sum)
