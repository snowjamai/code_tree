a = input()
# len_a = len(a)


def get_encoding(num):
    dict_num = []

    for i in num:
        if dict_num == []:
            dict_num.append((i, 1))
        else:
            if dict_num[-1][0] == i:
                dict_num[-1] = (i, dict_num[-1][1] + 1)
            else:
                dict_num.append((i,1))

    return dict_num 

def calc_len(num_list):
    cnt = 0

    for i in num_list:
        s1 = len(i[0])
        s2 = len(str(i[1]))
        cnt += s1 + s2 
    return cnt 

min_len = float('inf')
for i in range(len(a)):
    arr = a[-i:] + a[:-i]
    tmp = get_encoding(arr)
    lt = calc_len(tmp)
    if lt < min_len:
        min_len = lt


print(min_len)