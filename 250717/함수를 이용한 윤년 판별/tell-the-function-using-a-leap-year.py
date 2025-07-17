y = int(input())

# Please write your code here.

if y % 100 == 0  and y % 400 != 0:
    print("false")
else:
    if y % 4 == 0:
        print("true")
    else:
        print("false")
