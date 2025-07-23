arr = [0] * 2001 

base_pos = 1000

N = int(input())

for i in range(N):
    a, b = map(str, input().split())
    if b == 'R':
        target_pos = base_pos + int(a)

        for i in range(base_pos, target_pos):
            arr[i] += 1 
        base_pos = target_pos
    elif b == 'L':
        target_pos = base_pos - int(a) 
        
        for i in range(target_pos, base_pos):
            arr[i] += 1 
        base_pos = target_pos 
    
sum_v = 0
for i in range(2001):
    if arr[i] >= 2:
        sum_v += 1

print(sum_v)