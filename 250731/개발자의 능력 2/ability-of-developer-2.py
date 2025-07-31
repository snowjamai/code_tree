arr = list(map(int, input().split()))

arr.sort()

re1 = arr[0] + arr[-1]
re2 = arr[1] + arr[-2]
re3 = arr[2] + arr[-3]

if re1 < re2:
    tmp = re1 
    re1 = re2 
    re2 = tmp 
if re1 < re3:
    tmp = re3 
    re3 =re1
    re1 = tmp 
if re2 < re3:
    tmp = re2
    re2 = re3 
    re3 = tmp 

print(re1 - re3 )