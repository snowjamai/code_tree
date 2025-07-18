N = int(input()) 

arr = list(map(int, input().split())) 

def make_abs(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = -1 * arr[i] 
    
make_abs(arr) 

for i in arr:
    print(i, end=' ')