N = int(input()) 

def get_strange(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2 
    else:
        return get_strange(n // 3) + get_strange(n - 1)

print(get_strange(N))