def calc(arr):
    if(( 'G' in arr) and ('H' not in arr)) or ( 'H' in arr) and ('G' not in arr):
        return True 

    elif "G" in arr and 'H' in arr:
        cnt_g = 0
        cnt_h = 0
        for i in arr:
            if i == 'G':
                cnt_g += 1
            elif i == 'H':
                cnt_h += 1 
        if cnt_g == cnt_h and cnt_g != 0:
            return True 
    return False 


N = int(input())

s = [0] * 101 

for i in range(N):
    a, b = map(str, input().split())

    s[int(a)] = b 

max_v = 0

for i in range(101):
    for j in range(i, 101):
        if s[i] != 0 and s[j] != 0:
            tmp = s[i: j + 1] 
            if calc(tmp) == True:
                if max_v < (j - i):
                    max_v = j - i

print(max_v)


        