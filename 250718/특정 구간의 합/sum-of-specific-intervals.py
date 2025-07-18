N, M = map(int, input().split()) 

A = list(map(int, input().split())) 

for i in range(M):
    a, b = map(int, input().split()) 
    
    sum_t = 0 
    for j in range(a - 1, b):
        sum_t += A[j]
    
    print(sum_t)