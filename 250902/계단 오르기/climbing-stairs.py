dp = [0] * 10001 

dp[1] = 0
dp[2] = 1
dp[3] = 1

N = int(input())

for i in range(N + 1):
    if i <= 3:
        continue 
    else:
        dp[i] = dp[ i - 2] + dp[i - 3] 

print(dp[N] % 10007)