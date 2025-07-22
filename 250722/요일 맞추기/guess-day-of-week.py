m1,d1,m2,d2 = map(int, input().split()) 

sum_d1 = 0
for i in range(1,m1):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i ==12:
        sum_d1 += 31 
    elif i == 2:
        sum_d1 += 28 
    else:
        sum_d1 += 30 
sum_d1 += d1 

sum_d2 = 0
for i in range(1,m2):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i ==12:
        sum_d2 += 31 
    elif i == 2:
        sum_d2 += 28 
    else:
        sum_d2 += 30 
sum_d2 += d2 

diff = (sum_d2 - sum_d1) % 7


if diff == 0:
    print("Mon") 
elif diff == 1:
    print("Tue") 
elif diff == 2:
    print("Wed") 
elif diff == 3:
    print("Thu") 
elif diff == 4:
    print("Fri") 
elif diff == 5:
    print("Sat") 
elif diff == 6:
    print("Sun") 