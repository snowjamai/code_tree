N  = int(input()) 

arr = []
for i in range(N): 
    a, b, c, d= map(str, input().split()) 
    
    arr.append((a,int(b), int(c), int(d)))

arr.sort(key=lambda x: (x[1] + x[2] + x[3]))


for i in arr:
    print(i[0], i[1], i[2], i[3])