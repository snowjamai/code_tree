N = int(input()) 

def recur_func(n, cnt):
    if n == 1:
        return cnt 
    else:
        if n % 2 == 0:
            return recur_func(int(n/2), cnt + 1)
        else:
            return recur_func(n // 3, cnt + 1)

print(recur_func(N,0))

