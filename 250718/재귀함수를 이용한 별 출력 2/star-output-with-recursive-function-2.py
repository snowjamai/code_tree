N = int(input())


def recur_pr(n):
    if n < 1:
        return 
    
    for i in range(n):
        print("*", end=" ")
    print("")
    recur_pr(n - 1)
    
    for i in range(n):
        print("*", end=" ")
    print("")

recur_pr(N)