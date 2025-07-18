a, b = map(int, input().split()) 

if a > b:
    a += 25
    b *= 2
else:
    b += 25
    a *=2 
print(a, b)