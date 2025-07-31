arr = list(map(int, input().split()))

arr.sort()

re1 = arr[0] + arr[-1]
re2 = arr[1] + arr[-2]
re3 = arr[2] + arr[-3]
re = []
re.append(re1)
re.append(re2)
re.append(re3)

re.sort()
print(re[2] - re[0] )