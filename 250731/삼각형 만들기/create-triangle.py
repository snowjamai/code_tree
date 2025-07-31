
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
            tmp = [get_dist(arr[i], arr[j]), get_dist(arr[i], arr[k]), get_dist(arr[j], arr[k])]

            tmp.sort()
            if tmp[2] == tmp[1] + tmp[0]:
                s = (tmp[1] * tmp[0]) ** 0.5 
                if max_s < s :
                    max_s = s 


print(int(max_s))
