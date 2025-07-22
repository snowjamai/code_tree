arr = [0] * 201 

N = int(input())

for i in range(N):
    a, b = map(int, input().split()) 
    a, b = a + 100, b + 100 

    for j in range(a, b):
        arr[j] += 1
    
max_v = 0
for i in range(201):
    if max_v < arr[i]:
        max_v = arr[i]

print(max_v)
