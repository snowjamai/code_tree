N = int(input())

arr = list(map(int, input().split()))

cnt  = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        num_list = arr[i:j + 1] 
        num_sum = sum(num_list)
        num_avg = num_sum / len(num_list)
        yes = False
        for k in num_list:
            if num_avg == k:
                yes = True 
                # print(i, j 
        if yes == True:
            cnt += 1

print(cnt)
