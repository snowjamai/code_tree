class wether:
    def __init__(self, date, day, cast):
        self.date = date 
        self.day =day 
        self.cast = cast 
        self.num_date = int(date[:4] + date[5:7] + date[8:10])

arr = [] 

n = int(input()) 

for i in range(n):
    a, b, c = map(str,input().split()) 
    if c == 'Rain':
        tmp = wether(a, b, c) 
     

        arr.append(tmp)

arr.sort(key=lambda x:x.num_date) 

print(arr[0].date, arr[0].day, arr[0].cast)
