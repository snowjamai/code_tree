N = int(input()) 

def get_sum(n, total):
    if  n > N:
        return total
    else:
        return get_sum(n + 1, total + n)
        

print(get_sum(0,0))