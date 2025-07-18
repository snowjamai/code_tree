N, M = map(int, input().split()) 

arr = list(map(int, input().split()))

tot = 0
while M != 1: 
    tot += arr[M - 1]
  
    if M % 2 != 0:
        M -= 1 
    else:
        M = int( M / 2 )
tot += arr[0]
print(tot)

    