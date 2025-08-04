N, C, G, H = map(int, input().split()) 

arr = []

for i in range(N):
    a, b = map(int,input().split())

    arr.append((a,b))

max_work = 0 
for i in range(1001):
    work = 0
    for j in range(N):
        if i < arr[j][0]:
            work += C
        elif i <= arr[j][1]:
            work += G 
        elif i > arr[j][1]:
            work += H 
    if max_work < work:
        max_work = work 

print(max_work )
            