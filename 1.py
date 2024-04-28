
s, t = input().split()

def func(s, t):
    myset = set()
    for c in s:
        myset.add(c)
    for c in t:
        if c not in myset:
            return -1

    res = 0
    i = 0
    while i < len(t):
        j = 0
        while i < len(t) and j < len(s):
            if s[j] != t[i]:
                j += 1
            else:
                # print('j = ', j, s[j], end = '\n')
                i += 1
                j += 1
        res += 1
        # print()
    return res

print(func(s, t))
