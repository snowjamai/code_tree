
N, M = map(int, input().split()) 

a = [False] * 1000001
b = [False] * 1000001


a_t = 0
for i in range(N):
    v, t = map(int, input().split())
    for j in range(a_t + 1, a_t + 1 + t): 
        a[j] = a[j - 1] + v
    a_t = a_t + t 

b_t = 0
for i in range(M):
    v, t = map(int, input().split())
    for j in range(b_t + 1, b_t + 1 + t):
        b[j] = b[j - 1] + v 
    b_t = b_t + t 

comb = 0
cnt = 0
for i in range(1,a_t + 1):
    if a[i] > b[i] and comb != 1:
        comb = 1    
        cnt += 1
    elif a[i] == b[i] and comb != 0:
        comb = 0
        cnt += 1 
    elif a[i] < b[i] and comb != 2:
        cnt += 1
        comb = 2

print(cnt)