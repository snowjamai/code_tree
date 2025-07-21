class agent:
    def __init__(self, name, score):
        self.name = name 
        self.score =  score 

arr = []
for i in range(5):
    a, b = map(str, input().split())
    arr.append(agent(a,int(b)))
    
arr.sort(key= lambda x:x.score)
print(arr[0].name, arr[0].score)
