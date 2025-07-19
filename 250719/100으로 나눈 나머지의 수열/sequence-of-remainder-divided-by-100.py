N = int(input()) 

def mult_cnt(num):
    if num == 1:
        return 2
    elif num == 2:
        return 4
    else:
        return (mult_cnt(num - 1) * mult_cnt (num-2)) % 100

print(mult_cnt(N))
   