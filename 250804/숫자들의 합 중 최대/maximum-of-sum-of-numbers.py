
X, Y = map(int, input().split())

def get_sum(num):
    str_num = str(num)
    sum_v = 0
    for i in str_num:
        sum_v += int(i)
    return sum_v

max_v = 0
for i in range(X, Y + 1):
    tmp = get_sum(i)
    if tmp > max_v:
        max_v= tmp

print(max_v)

