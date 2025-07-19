a, b, c = map(int, input().split()) 

tot = a * b * c

def get_sum(num, sum_v):
    if num == 0:
        return sum_v 

    else:
        return get_sum(num // 10, sum_v + num % 10)

print(get_sum(tot, 0))