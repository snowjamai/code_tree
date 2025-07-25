N, M = map(int, input().split())

a = [False] * 1000002
b = [False] * 1000002

a[0] = 0
b[0] = 0

a_t = 0 
for i in range(N):
    x, d = map(str, input().split())
    if d == 'R':
        for j in range(a_t + 1, a_t + 1 + int(x)):
            a[j] = a[j - 1] +  1
    elif d == 'L':
        for j in range(a_t + 1, a_t + 1 + int(x)):
            a[j] = a[j - 1] -  1
    a_t += int(x) 

b_t = 0
for i in range(M):
    x, d = map(str, input().split())
    if d == 'R':
        for j in range(b_t + 1, b_t + 1 + int(x)):
            b[j] = b[j - 1] +  1
    elif d == 'L':
        for j in range(b_t + 1, b_t + 1 + int(x)):
            b[j] = b[j - 1] -  1
    b_t += int(x) 

max_t = 0
if a_t < b_t:
    max_t = b_t
    for i in range(a_t + 1, b_t + 1):
        a[i] = a[a_t]
    
else:
    max_t = a_t
    for i in range(b_t + 1, a_t + 1):
        b[i] = b[b_t]

cnt = 0 
for i in range(1,max_t + 1):
    if a[i] == b[i] and a[i - 1] != b[i - 1]:
        cnt += 1
print(cnt)
