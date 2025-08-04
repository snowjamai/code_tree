T, a, b = map(int, input().split())

S = []
N = []
for i in range(T):
    c, x = map(str, input().split())
    if c == 'S':
        S.append(int(x))

    elif c == 'N':
        N.append(int(x))


cnt = 0
for i in range(a, b + 1):
    s_min = float('inf')
    n_min = float('inf')
    for j in S:
        s_dist = abs(i - j)
        if s_dist < s_min:
            s_min = s_dist 
    for j in N:
        n_dist = abs(i - j)
        if n_dist < n_min:
            n_min = n_dist 

    if s_min <= n_min:
        cnt += 1


print(cnt)