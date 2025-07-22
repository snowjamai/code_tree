N , B = map(int, input().split()) 

arr = []
if B == 8:
    while N:
        arr.append(str(N % 8))
        N = N // 8 
elif B == 4:
    while N:
        arr.append(str(N % 4))
        N = N // 4
re = ''.join(arr[::-1]) 
print(re)