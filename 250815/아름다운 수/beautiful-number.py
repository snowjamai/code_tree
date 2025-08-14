N = int(input())

# Please write your code here.

cnt = 0 
def check(arr):
    idx = 0
    while arr != []:
        if arr[idx] == 1:
            arr = arr[1:]
        elif arr[idx] == 2:
            if len(arr) < 2:
                return False 
            if arr[idx] == arr[idx + 1]:
                arr = arr[idx +2:]
            else:
                return False 
        elif arr[idx] == 3:
            if len(arr)< 3:
                return False 
            if arr[0] == arr[1] and arr[2] == arr[1]:
                arr = arr[3:]
            else:
                return False 
        elif arr[0] == 4:
            if len(arr) < 4:
                return False
            if arr[0] == arr[1] and arr[2] == arr[3] and arr[3] == arr[0]:
                arr = arr[4:]
            else:
                return False
    return True 

        

def beautiful(l):
    global cnt 

    if len(l) >= N:
        c = check(l)
        if c == True:
            cnt += 1
    else:
        for i in range(1, 5):
            l.append(i)
            beautiful(l)
            l.pop() 
        

# N = int(input())

beautiful([])

print(cnt)



