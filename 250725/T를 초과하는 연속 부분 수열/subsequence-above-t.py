N, T = map(int, input().split()) 

arr = list(map(int,input().split()))


cnt = 0
max_cnt = 0
for i in range(N):
    if arr[i] > T:
        cnt += 1 
    else:
        if max_cnt < cnt:
            max_cnt = cnt 
        cnt = 0 

if max_cnt < cnt:
    max_cnt = cnt 

print(max_cnt)

