m1,d1,m2,d2 = map(int, input().split()) 
date = input() 
sum_d = 0
for i in range(m1,m2):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum_d += 31 
    elif i == 2:
        sum_d += 29 
    else:
        sum_d += 30 

sum_d = sum_d - d1 + d2 

date_cnt = sum_d // 7 
date_remain = sum_d % 7 

if date == 'Mon':
    target_date = 0
elif date == 'Tue':
    target_date = 1 
elif date == 'Wed':
    target_date = 2
elif date == 'Thu':
    target_date = 3
elif date == 'Fri':
    target_date = 4
elif date == 'Sat':
    target_date = 5
elif date == 'Sun':
    target_date = 6
if date_remain >= target_date:
    date_cnt += 1

print(date_cnt)