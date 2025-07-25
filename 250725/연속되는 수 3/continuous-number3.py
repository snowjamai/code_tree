N = int(input()) 

arr = []
for i in range(N):
    arr.append(int(input()))

cnt = 0 
max_cnt = 0
for i in range(N):
    if i == 0 or arr[i] * arr[i - 1] > 0 :
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt 
        cnt = 1
        
if max_cnt < cnt:
    max_cnt = cnt 

print(max_cnt)
        
    