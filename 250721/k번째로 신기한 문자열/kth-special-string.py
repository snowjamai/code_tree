N, K, T = map(str, input().split()) 
N, K = int(N), int(K)
arr = []
for i in range(N):
    arr.append(input()) 

tar_arr = [] 
for i in arr:
    if i[:len(T)] == T:
        tar_arr.append(i) 

tar_arr = sorted(tar_arr) 

print(tar_arr[K - 1])

