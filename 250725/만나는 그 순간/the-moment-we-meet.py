N, M = map(int, input().split())

a, b = 0, 0

arr_a = [False] * 1000001
arr_b = [False] * 1000001

arr_a[0], arr_b[0] = 0, 0
for i in range(N):
    d, x = map(str, input().split()) 
    if d == 'L':
        for j in range(a + 1, a + 1 + int(x)):
            arr_a[j] = arr_a[j - 1] - 1
        a = a + int(x)
    elif d == 'R':
        for j in range(a + 1, a + 1 + int(x)):
            arr_a[j] = arr_a[j - 1] + 1
        a += int(x)

for i in range(M):
    d, x = map(str, input().split()) 
    if d == 'L':
        for j in range(b + 1, b + 1 + int(x)):
            arr_b[j] = arr_b[j - 1] - 1
        b += int(x)
    elif d == 'R':
        for j in range(b + 1, b + 1 + int(x)):
            arr_b[j] = arr_b[j - 1] + 1
        b += int(x)

comp = False
for i in range(1000001):
    if arr_a[i] != False and arr_a[i] == arr_b[i]:
        comp = True 
        print(i)
        break 
if comp == False:
    print("-1")