Y, M, D = map(int, input().split())

# Please write your code here.

if Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
    max_2d = 29 
elif Y % 4 == 0 and Y % 100 == 0:
    max_2d = 28 
elif Y % 4 == 0:
    max_2d = 29
else:
    max_2d = 28 


if M == 3 or M == 4 or M == 5:
    if M == 3 or M == 5:
        if D <= 31:
            print("Spring")
    else:
        if D <= 30:
            print("Spring")
        else:
            print("-1")

    
if M == 6 or M == 7 or M == 8:
    if M == 7 or M == 8:
        if D <= 31:
            print("Summer")
    else:
        if D <= 30:
            print("Summer")
        else:
            print("-1")
        

if M == 9 or M ==10 or M == 11:
    if M == 9 or M == 1:
        if D <= 30:
            print("Fall")
    else:
        if D <= 31:
            print("Fall")
        else:
            print("-1")


if M == 12 or M ==1:
    if D <= 31:
        print("Winter")
    else:
        print("-1") 

if M == 2:
    if D > max_2d:
        print("-1")
    else:
        print("Winter")