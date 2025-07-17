n1, n2 = map(int, input().split())
a = list(map(str, input().split()))
b = list(map(str, input().split()))

# Please write your code here.

str_a = ''.join(a)
str_b = ''.join(b)
if str_b in str_a:
    print("Yes")
else:
    print("No")