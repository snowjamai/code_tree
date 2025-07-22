m1,d1,m2,d2 = map(int, input().split()) 

sum_d = 0
for i in range(m1, m2):
    if i == 2:
        sum_d += 28
    elif i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum_d += 31 
    else:
        sum_d += 30 

sum_d = (sum_d - d1) + 1
sum_d += d2 

print(sum_d)