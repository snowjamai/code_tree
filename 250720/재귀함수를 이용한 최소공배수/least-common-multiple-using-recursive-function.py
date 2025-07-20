n = int(input()) 

def get_gcd(a, b):
    if b == 0: return a
    else:
        return get_gcd(b, a % b)


num_list = list(map(int, input().split()))

re = 1
for i in num_list:
    re = int((re * i) / get_gcd(re, i))
print(re)