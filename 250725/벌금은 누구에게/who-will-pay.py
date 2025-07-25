N, M, K = map(int, input().split())

arr = [0] * (N + 1)

first = False
num = -1 
for i in range(M):
    k = int(input())
    arr[k] += 1

    for i in range(N + 1):
        if arr[k] >= K and first == False:
            first = True 
            num =  k 

    
print(num)
