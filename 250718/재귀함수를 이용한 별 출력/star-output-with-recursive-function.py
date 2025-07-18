N = int(input()) 

def print_star(num):
    
    for i in range(num):
        print("*",end = '')
    print("")
    if N == num:
        return 
    print_star(num + 1)
    


print_star(1)