N = int(input()) 

arr = []
while N:
    arr.append(str(N % 2))
    N = N // 2 
if arr == []:
    arr = ['0']
print(''.join(arr[::-1]))
    