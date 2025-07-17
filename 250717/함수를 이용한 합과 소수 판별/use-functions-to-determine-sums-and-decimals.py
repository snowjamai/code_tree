a, b = map(int, input().split())

# Please write your code here.
def is_so(num):
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True 
def get_all_sum(num):
    str_num = str(num) 
    cnt = 0
    for j in range(len(str_num)):
        cnt += int(str_num[j]) 
    return cnt 

cnt = 0
for i in range(a, b + 1):
    if is_so(i) == True:

        if get_all_sum(i) % 2 == 0: 
            cnt += 1
print(cnt)
