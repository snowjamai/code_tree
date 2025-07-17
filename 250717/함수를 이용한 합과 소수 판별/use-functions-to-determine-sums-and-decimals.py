a, b = map(int, input().split())

# Please write your code here.
def is_so(num):
    for i in range(2, num):
        if num % i == 0:
            return False 
    return True 

cnt = 0
for i in range(a, b + 1):
    if is_so(i) == True:
        if i % 2 == 0: 
            cnt += 1
print(cnt)
