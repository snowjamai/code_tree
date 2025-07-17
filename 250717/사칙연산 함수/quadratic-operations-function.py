a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

if o == '+':
    print(a, '+', c, '=',a+c,sep = ' ')
elif o == '-':
    print(a, '-', c, '=',a-c,sep = ' ')
elif o == '*':
    print(a, '*', c, '=',a*c,sep = ' ')
elif o == '/':
    print(a, '/', c, '=',a//c,sep = ' ')
else:
    print("False")
