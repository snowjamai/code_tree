dp = [0] * 1001

dp[1] = 1
dp[2] = 2 
dp[3] = 3

N = int(input())

for i in range(N + 1):
    if i <= 3:
        continue 
    dp[i] = dp[i - 2]+ dp[i - 1] 

print(dp[N])

