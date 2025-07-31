arr = list(map(int, input().split()))
sum_arr = sum(arr)
is_re = False
min_re = float('inf')
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            for k in range(len(arr)):
                if i != k and j != k:
                    for l in range(len(arr)):
                        if i != l and j != l and k != l:
                            sum1 = arr[i] + arr[j]
                            sum2 = arr[k] + arr[l]
                            sum3 = sum_arr - sum1 - sum2 
                            if sum1 == sum2 or sum1 == sum3 or sum2 == sum3:
                                continue 
                            else:
                                is_re = True 
                                re = [] 
                                re.append(sum1)
                                re.append(sum2)
                                re.append(sum3)
                                re.sort() 
                                if min_re > (re[2] - re[0]):
                                    min_re = re[2] - re[0]
                                # print(re[2]- re[0]) 

if is_re == False:
    print("-1")
else:
    print(min_re)