N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))

def find_bomb(arr):
    cnt = 1
    for i in range(len(arr)):
        if i == 0:
            continue 
        else:
            if arr[i] == arr[i -1]:
                cnt += 1
            else:
                if cnt >= M:
                    return True
                cnt = 1 
    if cnt >= M:
        return True 
    return False 

def bomb(arr):
    cnt = 1
    bs = 0
    for i in range(len(arr)):
        if i == 0:
            continue 
        else:
            if arr[i] == arr[i - 1]:
                cnt += 1
                
            else:
                if cnt >= M:
                    for j in range(bs, i):
                        arr[j] = -1 
                    bs = i 
                    cnt = 1
                else:
                    cnt = 1
                    bs = i 
    if cnt >= M:
        for j in range(bs, len(arr)):
            arr[j] = -1 
    tmp = [] 

    for i in arr:
        if i != -1:
            tmp.append(i)

    return tmp
b = arr 
is_b = False 

while find_bomb(b) == True:
    is_b = True 
    b = bomb(b)
 

if is_b == False:
    print("0")
else:
    print(len(b))
    for i in b:
        print(i)