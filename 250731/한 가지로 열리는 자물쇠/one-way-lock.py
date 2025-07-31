N = int(input())
a, b, c = map(int, input().split())

cnt = 0

for i in range(1, N +1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if abs(i - a) <= 2:
                cnt += 1
            else:
                if abs(j - b) <= 2:
                    cnt += 1
                else:
                    if abs(k - c) <= 2:
                        cnt += 1

    
print(cnt)