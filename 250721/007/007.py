arr = list(map(str, input().split()))


class a:
    def __init__(self, a, b, c):
        self.code = a 
        self.point= b
        self.t = c 


b = a(arr[0], arr[1], arr[2])

print(f"secret code : {b.code}")
print(f"meeting point : {b.point}")
print(f"time : {b.t}")