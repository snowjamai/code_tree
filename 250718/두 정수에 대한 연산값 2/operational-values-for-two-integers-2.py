a, b = map(int, input().split()) 

if a > b:
    b += 10
    a *= 2 

else:
    a += 10
    b *= 2
print(a, b)