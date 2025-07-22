a = input()

b = a[::-1]

re = 0
mul = 1
for i in range(len(b)):
    re = re + mul * int(b[i])
    mul = mul * 2 

print(re)

