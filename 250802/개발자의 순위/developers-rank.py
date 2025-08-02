K, N = map(int, input().split())


arr = []
for i in range(K):
    arr.append(list(map(int, input().split())))


def comp_ab(a, b):
    always = False 

    for i in  arr:
        for j in range(len(i)):
            if i[j] == a:
                a_i = j
            elif i[j] == b:
                b_i = j
        if a_i < b_i:
            always = True 
        else:
            return False

    return always

cnt = 0 
for i in range(1, N + 1 ):
    for j in range(1, N + 1):
        if i == j:
            continue 
        else:
            if comp_ab(i, j) == True:
                cnt += 1
print(cnt)
        

