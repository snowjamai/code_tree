n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
is_in = False 
for i in range(len(a)):
    if a[i] == b[0]:
        is_in = False 
        for j in range(i, i + len(b)):
            if a[j] == b[j - i]:
                is_in = True 
                continue 
            else:
                is_in = False
                break 
    if is_in == True:
        print("Yes")
        break
if is_in == False:
    print("No")

        