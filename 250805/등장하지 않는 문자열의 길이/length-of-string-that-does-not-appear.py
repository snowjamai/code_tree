N = int(input())
s = input() 

min_len = N

for i in range(1, N + 1):
    is_dupli = False 
    for j in range(N):
        con_str = s[j:j + i]
        left = s[j + 1:]
        if con_str in left:
            is_dupli = True 
    if is_dupli == False:
        if min_len > i:
            min_len = i 
print(min_len)

            