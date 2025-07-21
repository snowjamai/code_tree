class bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec 

code, color, sec = map(str, input().split()) 

print(f"code : {code}")
print(f"color : {color}")
print(f"second : {sec}")
