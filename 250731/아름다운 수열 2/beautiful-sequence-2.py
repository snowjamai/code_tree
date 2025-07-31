N, M = map(int, input().split())

A = list(map(int,input().split()))
B=list(map(int,input().split()))


B. sort()
cnt = 0 
for i in range(len(A) - len(B) + 1):
    tmp = A[i:i + len(B)]
    
    tmp.sort()

    if tmp == B:
        cnt += 1 

print(cnt)