N, S = map(int, input().split())

arr = list(map(int, input().split()))


sub_min = float('inf')
for i in range(len(arr) - 1):
    for j in range(i + 1 , len(arr)):
        num_sum = 0 
        for k in range(len(arr)):
            if k == i or k == j:
                continue 
            else:
                num_sum += arr[k]
        sub = abs(num_sum - S)
        if sub < sub_min:
            sub_min = sub

print(sub_min)
            
        