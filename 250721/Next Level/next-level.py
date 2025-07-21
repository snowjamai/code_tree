class s:
    def __init__(self, uid='codetree', level=10):
        self.uid = uid 
        self.level = level 

c, d = map(str, input().split())
a = s() 
b = s(c, int(d))

print(f"user {a.uid} lv {a.level}")
print(f"user {b.uid} lv {b.level}")
