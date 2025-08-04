X, Y = map(int, input().split())

def get_interesting(num):
    str_num = str(num)
    num_dict = {} 

    for i in str_num:
        if int(i) not in num_dict:
            num_dict[int(i)] = 1
        else:
            num_dict[int(i)] += 1 
    if len(num_dict) == 2:
        first = False 
        second = False
        for j in num_dict.values():
            if first == False:
                first = j
            else:
                second = j
        if first == 1 or second == 1:
            return True 
    return False

cnt = 0
for i in range(X, Y + 1):
    tmp = get_interesting(i)
    if tmp == True: 

        cnt += 1 

print(cnt)