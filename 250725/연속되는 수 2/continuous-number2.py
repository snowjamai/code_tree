N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))
    
arr.sort()
max_cnt = 0
cnt = 0

for i in range(len(arr)):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1 
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 0
    
if max_cnt < cnt:
    max_cnt = cnt
print(max_cnt)
        
    