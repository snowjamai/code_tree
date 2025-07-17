a, b = map(int, input().split())

# Please write your code here.

def get_three(num):
    if num == 0:
        return False 
    else:
        if (num % 10) == 3 or (num % 10) == 6 or (num % 10) == 9:
            return True 
        else:
            return get_three(num // 10) 

cnt = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        cnt += 1 
    else:
        if get_three(i) == True:
            cnt += 1

print(cnt)

