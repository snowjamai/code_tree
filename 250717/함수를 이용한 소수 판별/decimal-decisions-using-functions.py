a, b = map(int, input().split())

# Please write your code here.

def get_so(a, b):
    tmp = [False] * (b+ 1) 
    for i in range(2, b + 1):
        if tmp[i] == False:
            for j in range(2 * i, b + 1, i):
                tmp[j] = True 

    cnt = 0
    for i in range(a, b+1):
        if tmp[i] == False:
            cnt += i

    return cnt 

print(get_so(a, b))