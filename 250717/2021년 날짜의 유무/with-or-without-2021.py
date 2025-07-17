M, D = map(int, input().split())

# Please write your code here.

if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
    if D > 31:
        print("No")
    else:
        print("Yes")
elif M == 2:
    if D > 28:
        print("No")
    else:
        print("Yes")
elif M == 4 or M == 6 or M == 9 or M == 11:
    if D > 30:
        print("No")
    else:
        print("Yes")
else:
    print("No")