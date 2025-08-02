N, K = map(int, input().split())

arr = []

for i in range(N):
    arr.append(int(input()))



def get_idx(num):
    tmp = []
    for i in range(len(arr)):
        if arr[i] == num:
            tmp.append(i)

    return tmp 

bomb_num = -1
for i in range(N):
    tmp = get_idx(i) 
    if tmp == []: 
        continue 
    elif len(tmp) == 1:
        continue 
    else:
        tmp.sort() 
        for j in range(len(tmp) - 1):
            if tmp[j + 1] - tmp[j]  <= K:
                numb = i 
                if bomb_num < numb:
                    bomb_num = numb 

print(bomb_num)
                

    
