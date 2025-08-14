

def comb(l):
    if len(l) >= N:
        print(l[0], l[1])

    else:
        for i in range(1, K + 1):
            l.append(i) 
            # print(l)
            comb(l)
            l.pop()          
    

K, N = map(int, input().split())

comb([])
# print(t)

