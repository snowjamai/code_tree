s = input()
max_v = 0 



        
if 'f' in s:
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    for e in range(1,5):
                        for f in range(1,5):
                            mapper = {
                                "a":a,
                                "b":b,
                                "c":c,
                                "d":d,
                                "e":e,
                                "f":f
                            }
                            re = 0 
                            for i in range(len(s)):
                                if s[i] == '-':
                                    if i == 1:
                                        prev = mapper[s[i - 1]]
                                    else:
                                        prev = re 
                                    forw = mapper[s[i + 1]]
                                    re = prev - forw
                                elif s[i] == '*':
                                    if i == 1:
                                        prev = mapper[s[i - 1]]
                                    else:
                                        prev = re 
                                    forw = mapper[s[i + 1]]
                                    re = prev * forw
                                elif s[i] == '+':
                                    if i == 1:
                                        prev = mapper[s[i - 1]]
                                    else:
                                        prev = re
                                    forw = mapper[s[i + 1]]
                                    re = prev + forw
                            if max_v < re:
                                max_v = re 

elif 'e' in s:
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    for e in range(1,5):
                        mapper = {
                            "a":a,
                            "b":b,
                            "c":c,
                            "d":d,
                            "e":e
                        }
                        re = 0 
                        for i in range(len(s)):
                            if s[i] == '-':
                                if i == 1:
                                    prev = mapper[s[i - 1]]
                                else:
                                    prev = re 
                                forw = mapper[s[i + 1]]
                                re = prev - forw
                            elif s[i] == '*':
                                if i == 1:
                                    prev = mapper[s[i - 1]]
                                else:
                                    prev = re 
                                forw = mapper[s[i + 1]]
                                re = prev * forw
                            elif s[i] == '+':
                                if i == 1:
                                    prev = mapper[s[i - 1]]
                                else:
                                    prev = re 
                                forw = mapper[s[i + 1]]
                                re = prev + forw
                        if max_v < re:
                            max_v = re 
elif 'd' in s:
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    mapper = {
                        "a":a,
                        "b":b,
                        "c":c,
                        "d":d
                    }
                    re = 0 
                    for i in range(len(s)):
                        if s[i] == '-':
                            if i == 1:
                                prev = mapper[s[i - 1]]
                            else:
                                prev = re
                            forw = mapper[s[i + 1]]
                            re = prev - forw
                        elif s[i] == '*':
                            if i == 1:
                                prev = mapper[s[i - 1]]
                            else:
                                prev = re
                            forw = mapper[s[i + 1]]
                            re = prev * forw
                        elif s[i] == '+':
                            if i == 1:
                                prev = mapper[s[i - 1]]
                            else:
                                prev = re
                            forw = mapper[s[i + 1]]
                            re = prev + forw
                    if max_v < re:
                        max_v = re 
elif 'c' in s:
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                mapper = {
                    "a":a,
                    "b":b,
                    "c":c
                }
                re = 0 
                for i in range(len(s)):
                    if s[i] == '-':
                        if i == 1:
                            prev = mapper[s[i - 1]]
                        else:
                            prev = re 

                        forw = mapper[s[i + 1]]
                        re = prev - forw
                    elif s[i] == '*':
                        if i == 1:
                            prev = mapper[s[i - 1]]
                        else:
                            prev = re 
                        
                        forw = mapper[s[i + 1]]
                        re = prev * forw
                    elif s[i] == '+':
                        if i == 1:
                            prev = mapper[s[i - 1]]
                        else:
                            prev = re 
                        forw = mapper[s[i + 1]]
                        re = prev + forw
                   
                if max_v < re:
                    max_v = re 
elif 'b' in s:
    for a in range(1,5):
        for b in range(1,5):
            mapper = {
                "a":a,
                "b":b
            }
            re = 0 
            for i in range(len(s)):
                if s[i] == '-':
                    if i == 1:
                        prev = mapper[s[i - 1]]
                    else:
                        prev = re
                    forw = mapper[s[i + 1]]
                    re = prev - forw
                elif s[i] == '*':
                    if i == 1:
                        prev = mapper[s[i - 1]]
                    else:
                        prev = re
                    forw = mapper[s[i + 1]]
                    re = prev * forw
                elif s[i] == '+':
                    if i == 1:
                        prev = mapper[s[i - 1]]
                    else:
                        prev = re
                    forw = mapper[s[i + 1]]
                    re = prev + forw
            if max_v < re:
                max_v = re 

elif 'a' in s:
    mapper = {
        "a":a,
        "b":b,
        "c":c,
        "d":d,
        "e":e,
        "f":f
    }
    re = 0 
    for i in range(len(s)):
        if s[i] == '-':
            if i == 1:
                prev = mapper[s[i - 1]]
            else:
                prev = re
            forw = mapper[s[i + 1]]
            re = prev - forw
        elif s[i] == '*':
            if i == 1:
                prev = mapper[s[i - 1]]
            else:
                prev = re
            forw = mapper[s[i + 1]]
            re = prev * forw
        elif s[i] == '+':
            if i == 1:
                prev = mapper[s[i - 1]]
            else:
                prev = re
            forw = mapper[s[i + 1]]
            re = prev + forw
    if max_v < re:
        max_v = re 

print(max_v)