N, M = map(int, input().split())

a = [False] * 1000001
b = [False] * 1000001
a[0] = 0
b[0] = 0
a_t = 0
b_t = 0
for i in range(N):
    v , t = map(int, input().split())
    for j in range(a_t + 1, a_t + t + 1):
        a[j] = a[j-1] + v 
    
    a_t += t 

for i in range(M):
    v , t = map(int, input().split())
    for j in range(b_t + 1, b_t + t + 1):
        b[j] = b[j-1] + v 
    
    b_t += t 

sun = 0 
cnt = 0
for i in range(a_t + 1):
    if sun == 0:
        if a[i] > b[i]:
            sun = 1 
        elif b[i] > a[i]:
            sun = 2 
   
    elif sun == 1:
        if b[i] > a[i]:
            sun = 2 
            cnt += 1
    elif sun == 2:
        if a[i] > b[i]:
            sun = 1 
            cnt += 1

print(cnt)

