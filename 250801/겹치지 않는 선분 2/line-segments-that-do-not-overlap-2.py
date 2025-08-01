N = int(input())
arr = []

for i in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
    
def is_include(ax1,ax2, bx1,bx2):
    if ax1 < ax2:
        if bx1 < ax1:
            if bx2 < ax2:
                return False
            else:
                return True 
        else:
            if bx2 > ax2:
                return False 
            else:
                return True 
    else:
        if bx1 < ax1:
            if bx2 < ax2:
                return False
            else:
                return True 
        else:
            if bx2 < ax2:
                return True 
            else:
                return False 

cnt = 0
for i in range(N):
    target_1, target_2 = arr[i][0], arr[i][1]
    
    include = False 
    for j in range(N):
        if i != j:
            if is_include(arr[i][0], arr[i][1], arr[j][0],arr[j][1]) == True:
                include = True 
    if include == True:
        cnt += 1

print(cnt)


