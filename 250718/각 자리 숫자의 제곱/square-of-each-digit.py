N = int(input())

def get_sum(n, value ):
    if n == 0:
        return value 
    else:
    
        return get_sum(n // 10 , value + (n%10) *( n%10))

print(get_sum(N,0))