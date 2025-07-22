m1,d1,m2,d2 = map(int, input().split()) 

sum_d = 0
for i in range(m1, m2):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i ==12:
        sum_d += 31 
    elif i == 2:
        sum_d += 28 
    else:
        sum_d += 30 

sum_d = (sum_d - d1 + d2) % 7

if sum_d == 0:
    print("Mon") 
elif sum_d == 1:
    print("Tue") 
elif sum_d == 2:
    print("Wed") 
elif sum_d == 3:
    print("Thu") 
elif sum_d == 4:
    print("Fri") 
elif sum_d == 5:
    print("Sat") 
elif sum_d == 6:
    print("Sun") 