dp = [0] * 1000002


dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2

target = int(input())

for i in range(5, target + 2):
    if i % 2 == 0 and i % 3 == 0:
        if dp[i // 2] <= dp[i // 3]:
            dp[i] = dp[i // 2] + 1
        else:
            dp[i] = d[i // 3] + 1
    elif i % 2 == 0:
       
        dp[i] = dp[i // 2] + 1
    elif i % 3 == 0:
        dp[i] = dp[i // 3] + 1
    else:
            
        even_min = min(dp[(i -1)// 2] + 2, dp[(i + 1)// 2] + 2)
        if (i + 1) % 3 == 0:
            dp[i] = min(even_min, dp[(i + 1) // 3] + 2)

        elif (i - 1) % 3 == 0:
            dp[i] = min(even_min, dp[(i - 1) // 3] + 2)
        

            

print(dp[target])
        