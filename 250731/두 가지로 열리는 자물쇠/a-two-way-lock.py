N=int(input())

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

cnt = 0

mid_n = N // 2 

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            sub_a1 = abs(i - a1) 
            sub_b1 = abs(j - b1) 
            sub_c1 = abs(k - c1) 
        
            if sub_a1 > mid_n:
                sub_a1 = N - abs(i - a1)
            if sub_b1 > mid_n:
                sub_b1 = N - abs(j - b1)
            if sub_c1 > mid_n:
                sub_c1 = N - abs(k - c1)

            sub_a2 = abs(i - a2) 
            sub_b2 = abs(j - b2) 
            sub_c2 = abs(k - c2) 
        
            if sub_a2 > mid_n:
                sub_a2 = N - abs(i - a2)
            if sub_b2 > mid_n:
                sub_b2 = N - abs(j - b2)
            if sub_c2 > mid_n:
                sub_c2 = N - abs(k - c2)

            if sub_a1 <= 2 and sub_b1 <= 2 and sub_c1 <= 2:
                cnt += 1 
            elif sub_a2 <= 2 and sub_b2 <= 2 and sub_c2 <= 2:
                cnt += 1
print(cnt)
