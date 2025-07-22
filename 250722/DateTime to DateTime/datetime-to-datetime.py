A, B, C = map(int, input().split())

base_m = 10 * 24 * 60 + 11 * 60 + 11 

target_m = (A - 1) * 24 * 60 + B * 60 + C 

print(target_m - base_m)