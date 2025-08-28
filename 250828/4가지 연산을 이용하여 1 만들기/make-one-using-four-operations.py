dp = [0] * 1000002


dp[1] = 0
dp[2] = 1
dp[3] = 1
dp [4] = 2


def dfs(i):
    if i > target + 2 or i < 1:
        return 
    
    if i == 1:
        return 0
    elif i == 2:
        return 1
    elif i == 3:
        return 1 
    else:
        if i % 2 == 0:
            return min(min(dfs(i - 1) + 1, dfs(i + 1) + 1),dfs(i //2) + 1) 
        elif i % 3 == 0:
            return min(min(dfs(i - 1) + 1, dfs(i + 1) + 1),dfs(i //3) + 1) 
        else:
            return min(dfs(i - 1) + 1, dfs(i + 1) + 1)

target = 6 

print(dfs(target))