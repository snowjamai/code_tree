N, M  = map(int, input().split())

a_t = [0] * 100001
b_t = [0] * 100001


base_a = 0
base_t = 0
for i in range(N):
    d, t = map(str, input().split()) 
    if d == 'L':
        for j in range(base_t + 1, base_t + int(t) + 1):
            a_t[j] =a_t[j - 1] - 1 
        base_t += int(t)

    elif d == 'R':
        for j in range(base_t + 1, base_t + int(t) + 1):
            a_t[j] =a_t[j - 1] + 1 
        base_t += int(t)

        
base_b = 0
base_t = 0
for i in range(M):
    d, t = map(str, input().split()) 
    if d == 'L':
        for j in range(base_t + 1, base_t + int(t) + 1):
            b_t[j] =b_t[j - 1] - 1 
        base_t += int(t)

    elif d == 'R':
        for j in range(base_t + 1, base_t + int(t) + 1):
            b_t[j] =b_t[j - 1] + 1 
        base_t += int(t)


meet = False 
for i in range(1,100001):
    if a_t[i] == b_t[i]:
        meet= True 
        print(i)
        break

if meet == False:
    print("-1")
