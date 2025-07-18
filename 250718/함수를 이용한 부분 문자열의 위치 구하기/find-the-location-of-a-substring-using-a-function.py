N = input()
M = input()

def fine_nm(N, M):
    for i in range(len(N) - len(M) + 1):
        if N[i:i + len(M)] == M:
            return i 
    return -1 

print(fine_nm(N, M))
