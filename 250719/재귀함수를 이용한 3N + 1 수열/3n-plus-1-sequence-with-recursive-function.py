

N = int(input()) 

def cnt_num(n, cnt):
    if n == 1:
        return cnt 
    else:
        if n % 2 == 0 :
            return cnt_num(n//2, cnt + 1)
        else:
            return cnt_num(n * 3 + 1, cnt + 1)

print(cnt_num(N, 0))