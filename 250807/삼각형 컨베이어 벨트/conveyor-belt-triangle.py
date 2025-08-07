N, T = map(int, input().split())

arr = list(map(int,input().split())) + list(map(int,input().split())) + list(map(int,input().split()))


r = T % (3 * N)
arr = arr[-r:] + arr[:-r]
for i in range(len(arr)):
    print(arr[i] , end = ' ')
    if (i + 1) % N == 0:
        print("")