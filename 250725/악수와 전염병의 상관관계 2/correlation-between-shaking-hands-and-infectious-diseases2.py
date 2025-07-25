N, K, P, T = map(int, input().split())


arr = [0] * 251 
infect_man = [0] * 101 

infect_man[P] = K  
infect_p = [False] * 101 
infect_p[P] = True 

for i in range(T):
    t, x, y = map(int, input().split())
    arr[t] = (x, y) 

for i in range(251):
    if arr[i] == 0:
        continue 
    
    if infect_man[arr[i][0]] != 0:
        if infect_man[arr[i][1]] == 0:
            infect_man[arr[i][1]] = K 
            infect_p[arr[i][1]] = True 
        else:
            infect_man[arr[i][1]] -= 1
        infect_man[arr[i][0]] -= 1
    elif infect_man[arr[i][1]] != 0:
        if infect_man[arr[i][0]] == 0:
            infect_man[arr[i][0]] = K
            infect_p[arr[i][0]] = True 

        else:
            infect_man[arr[i][0]] -= 1
        infect_man[arr[i][1]] -= 1
 

for i in range(1, N + 1):
    if infect_p[i] == False:
        print("0",end='')
    else:
        print("1",end='')