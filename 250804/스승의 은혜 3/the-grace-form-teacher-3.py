N, B = map(int, input().split())

P, S = [], []
for i in range(N):
    p, s = map(int, input().split())
    P.append(p)
    S.append(s)
max_cnt = 0
for i in range(N):
    tmp = []
    for j in range(N):
        if j == i:
            tmp.append(P[j]//2 + S[j])
        else:
            tmp.append(P[j] + S[j])
    tmp.sort() 

    cnt = 0 
    s = 0
    for j in range(N):
        s += tmp[j]
        if s >B:
            if cnt > max_cnt:
                max_cnt = cnt 
        else:
            cnt += 1 
print(max_cnt) 
