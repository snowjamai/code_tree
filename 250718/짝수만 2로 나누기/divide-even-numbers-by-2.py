N = int(input()) 
arr = list(map(int, input().split()))

for i in arr:
    if i % 2 == 0:
        print(i // 2, end=' ')
    else:
        print(i, end = ' ')