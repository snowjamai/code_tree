N, T = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = b[::-1]
for i in range(T):
    tmp = a[N - 1]
    a = b[:1] + a[:N - 1]
    b = b[1:] + [tmp] 
b = b[::-1]

for i in a:
    print(i, end = ' ')
print("")
for i in b:
    print(i, end = ' ')