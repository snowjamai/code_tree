arr = [[0]* 200 for _ in range(200)]

N= int(input())

for i in range(N):
    x1,y1, x2, y2 = map(int, input().split()) 
    
    for h in range(y1 + 100, y2 + 100 ):
        for w in range(x1 + 100, x2 + 100):
            arr[h][w] = 1 

tot = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 1:
            tot += 1

print(tot)