N = int(input()) 

class people:
    def __init__(self, name, number, register):
        self.name = name
        self.number = number
        self.register = register

arr = []
for i in range(N):
    a, b, c = map(str, input().split())
    arr.append(people(a, b, c))

arr.sort(key= lambda x:x.name, reverse=True)

print(f"name {arr[0].name}")
print(f"addr {arr[0].number}")
print(f"city {arr[0].register}")