arr = []

for i in range(5):
    name, h, w = map(str, input().split()) 
    arr.append((name,int(h), float(w)))

print("name")
arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0], i[1], i[2])

print("\nheight")
arr.sort(key=lambda x:-x[1])

for i in arr:
    print(i[0], i[1], i[2])