N = int(input()) 

def print_star(N, cnt):
    if cnt == N:
        return 
    print("HelloWorld")
    print_star(N, cnt + 1)

print_star(N, 0)