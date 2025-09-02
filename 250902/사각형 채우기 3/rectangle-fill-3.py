N = int(input()) 

dp = [0] * 1001 

dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(N + 1):
    if i <= 3: 
        continue 

    dp[i] = (dp[i - 1] * 2 + dp[i - 2] ) % 1000000007

print(dp[N] )
