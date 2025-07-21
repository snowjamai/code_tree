N = int(input()) 

arr = list(map(int, input().split())) 

tar_arr = [] 
for i in range(len(arr)):
    tar_arr.append(arr[i])
    if i % 2 == 0:
        tar_arr.sort() 
        print(tar_arr[i//2], end= ' ')



