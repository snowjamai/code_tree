N = int(input())


def print_num(n):
    if n < 1 or n > N:
        return 
    print(n, end = ' ')
    print_num(n - 1)
    print(n, end = ' ')
    # print_num(n )

print_num(N)