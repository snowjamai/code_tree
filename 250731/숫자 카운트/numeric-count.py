
N = int(input())
arr = [] 

for i in range(N):
    A, B, C = map(str, input().split())
    arr.append((A,int(B),int(C)))

def get_strike(src, target):
    cnt = 0
    for i in range(3):
        if src[i] == target[i]:
            cnt += 1
    return cnt 

def get_ball(src, target):
    cnt = 0
    for i in range(3):
        if src[i] != target[i]:
            if src[i] in target:
                cnt += 1

    return cnt 
                   


cnt = 0

for i in range(1,10):
    for j in range(1, 10):
        for k in range(1, 10):
            can_num = False 
            for a in arr:
                target = a[0]
                src = str(i * 100 + j * 10 + k)
             
                st = get_strike(src, target)
                ba = get_ball(src, target) 
                if st == a[1] and ba== a[2]:
                    can_num = True 
                else:
                    can_num = False 
                if can_num == False:
                    break 
            if can_num == True:
                cnt += 1

print(cnt)
    
