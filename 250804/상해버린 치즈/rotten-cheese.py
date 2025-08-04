N, M, D, S = map(int, input().split())

person = [[[] for _ in range(101)] for _ in range(51)]

for i in range(D):
    p, m, t = map(int, input().split())
    person[p][t].append(m)

sick = []
def calc_spoil(cheese):
    cnt = 0
    for i in range(N + 1):
        spoil = False 
        for j in range(1, 51):
            if cheese in person[i][j]:
                spoil = True 
                break 
        if spoil == True:
            cnt += 1

    return cnt 


for i in range(S):
    p, t = map(int,input().split())
    sick.append((p, t))

max_cnt = 0
for i in range(1, M + 1):
    spoiled = False   

    for s in sick:
        p, t = s[0], s[1]
        
        for j in range(1, t):
            if i in person[p][j]:
                spoiled = True 
        if spoiled == False:
            break
    if spoiled == True:
        cnt = calc_spoil(i)
        if cnt > max_cnt:
            max_cnt = cnt 

print(max_cnt)






    
    
    