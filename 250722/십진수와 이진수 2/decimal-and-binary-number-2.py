N = input()

N = N[::-1]

re = 0
mul = 1
for i in range(len(N)):
    re += mul * int( N[i] )
    mul *= 2 

re *= 17 

arr = []
while re:
    arr.append(str(re % 2))
    re = re // 2

print(''.join(arr[::-1]))