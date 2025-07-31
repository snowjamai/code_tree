N, H , T = map(int, input().split())

arr = list(map(int, input().split()))

def calc_cost(num):
    cnt = 0
    for j in range(num, num + T):
        cnt += abs(arr[j] - H)
    return cnt 

min_v = float('inf')
for i in range(len(arr) - T + 1):
    re = calc_cost(i)
    # print(i, re)
    if min_v > re:
        min_v = re 


print(min_v)