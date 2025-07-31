N, H , T = map(int, input().split())

arr = list(map(int, input().split()))

def calc_cost(num):
    cnt = 0
    for i in range(num - T, num):
        cnt += abs(arr[i] - H)
    return cnt 

min_v = float('inf')
for i in range(T, len(arr)):
    re = calc_cost(i)
    if min_v >  re:
        min_v = re


print(min_v)