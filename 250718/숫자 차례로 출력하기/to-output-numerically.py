N = int(input())

def print_num(n, reverse = True):
    if reverse == True:
        if n == 0:
            return 
        else:
            print(n, end=' ')
            print_num(n-1, reverse)
    else:
        if n == N + 1:
            return 
        else:
            print(n, end= ' ')
            print_num(n + 1 , reverse)


print_num(1,False)
print('')
print_num(N,True)