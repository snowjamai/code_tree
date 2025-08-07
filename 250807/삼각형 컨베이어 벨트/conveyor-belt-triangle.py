N, T = map(int, input().split())

arr = list(map(int,input().split())) + list(map(int,input().split())) + list(map(int,input().split()))


r = T % (3 * N)
arr = arr[-r:] + arr[:-r]
for i in range(3):
    for j in range(N):
        print(arr[3 * i + j] , end = ' ')
    print("")