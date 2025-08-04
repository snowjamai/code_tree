def is_palin(num):
    str_num = str(num)
    len_num = len(str_num)
    for i in range(len_num// 2):
        if str_num[i] != str_num[len_num - i - 1]:
            return False 
    return True 


X, Y = map(int,input().split())

cnt = 0
for i in range(X, Y + 1):
    if is_palin(i) == True:
        cnt += 1

print(cnt)