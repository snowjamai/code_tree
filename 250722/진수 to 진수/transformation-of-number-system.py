A, B = map(int, input().split()) 

N = input()

N = N[::-1]

re = 0
mul = 1
for i in range(len(N)):
    re += int(N[i] )* mul 
    mul = mul * A 




arr = [] 

while re:
    arr.append(str(re % B))
    re = re // B 

print(''.join(arr[::-1]))