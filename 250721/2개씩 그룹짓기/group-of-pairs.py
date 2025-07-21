n = int(input()) 

arr = list(map(int, input().split()))

arr.sort() 

max_v = 0

for i in range(n):
    a, b = arr[i], arr[2*n - i - 1]
    sum_v = a + b 
    if sum_v > max_v:
        max_v = sum_v

print(max_v )