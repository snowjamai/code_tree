N = int(input())

arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = arr[: i] + arr[i + 1: j] + arr[j + 1: k] + arr[k + 1:]

            line = [0] * 101
            is_ok = True 
            for t in tmp:
                for m in range(t[0], t[1] + 1):
                    line[m] += 1 

            for t in range(101):
                if line[t] >= 2:
                    is_ok = False
                    break 

            if is_ok == True:
                cnt  += 1

print(cnt)
                    

            
    