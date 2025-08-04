A, B, C = map(int, input().split())

max_v = 0 

for i in range(1001):
    for j in range(1001):
        re = A * i + B*j
        if re <= C:
            if max_v < re:
                max_v = re

print(max_v)