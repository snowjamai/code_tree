
N = int(input())

arr = []
for i in range(N):
    x, y = map(int, input().split())

    arr.append((x,y))
    
def get_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1]) ** 2 

max_s = 0 

for i in range(N- 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if arr[i][0] == arr[j][0] and arr[j][0] == arr[k][0] or arr[i][1] == arr[j][1] and arr[j][1] == arr[k][1]:
                continue 
            else:
                s = 0
                if arr[i][0] == arr[j][0]:
                    h = abs(arr[i][1] - arr[j][1])
                    w = abs(arr[i][0] - arr[k][0])
                    s = h * w
                elif arr[j][0] == arr[k][0]:
                    h = abs(arr[j][1] - arr[k][1])
                    w = abs(arr[j][0] - arr[i][0])
                    s = h * w
                elif arr[i][0] == arr[k][0]:
                    h = abs(arr[i][1] - arr[k][1])
                    w = abs(arr[i][0] - arr[j][0])
                    s = h * w
                
                if max_s < s:
                    max_s = s 
                
print(int(max_s))
