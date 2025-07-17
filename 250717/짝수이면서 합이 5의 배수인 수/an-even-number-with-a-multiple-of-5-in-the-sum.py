n = int(input())

# Please write your code here.

a, b = n // 10, n % 10 
if (a + b) % 5 == 0:
    print("Yes")
else:
    print("No")