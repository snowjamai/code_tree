arr = list(map(int, input().split()))

tot_sum = sum(arr)
sub_min = float('inf')
for i in range(4):
    for j in range(i + 1, 5):
        for k in range(j + 1, 6):
            g1 = arr[i] + arr[j] + arr[k] 
            g2 = tot_sum - g1 
            sub = abs(g2- g1)
            if sub_min > sub:
                sub_min = sub
print(sub_min)
