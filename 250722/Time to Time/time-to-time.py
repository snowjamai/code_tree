A, B, C, D = map(int, input().split()) 

after_m = C * 60 + D 
before_m = A * 60 + B 

print(after_m - before_m)