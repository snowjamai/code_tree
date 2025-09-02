dp = [0] * 46

dp[1] = 1
dp[2] = 1
dp[3] = 2 
N = int(input()) 

for i in range(N + 1):
    if i <= 3:
        continue 
    else:
        dp[i] = dp[ i -1] + dp[i - 2]
print(dp[N])