

def comb(l):
    if len(l) >= N:
        if len(l) >= 2:
            for i in l:
                print(i, end=' ')
        else:
            print("1")

    else:
        for i in range(1, K + 1):
            l.append(i) 
            # print(l)
            comb(l)
            l.pop()          
    

K, N = map(int, input().split())

comb([])
# print(t)

