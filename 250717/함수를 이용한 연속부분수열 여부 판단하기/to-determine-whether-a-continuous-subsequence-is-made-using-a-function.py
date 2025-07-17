n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.

def is_in(a, b):
    check = False 
    for i in range(len(a) - len(b) + 1):
        if a[i] == b[0]:
            for j in range(i, i + len(b)):
                if a[j] == b[j - i]:
                    check = True 
                else:
                    check = False
                    break
            if check == True:
                return True 

    return False


if is_in(a, b) == False:
    print("No")
else:
    print("Yes")

        