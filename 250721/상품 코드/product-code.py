class product:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code

a = product()
b = product() 

c, d = map(str, input().split()) 
b.name = c 
b.code = int(d)

print(f"product {a.code} is {a.name}")
print(f"product {b.code} is {b.name}")