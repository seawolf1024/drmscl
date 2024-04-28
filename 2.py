


def func(a, b):
    for i in range(0, len(a)):
        stk = []
        for j in range(0, len(a[i])):
            if a[i][j] == '(':
                stk.append(j)
            elif a[i][j] == ')':
                if len(stk) == 0:
                    # ()))
                    b[i][j] = '?'
                else:
                    stk.pop()
        while len(stk) != 0:
            j = stk[-1]
            b[i][j] = 'x'
            stk.pop()
    #for x in b:
    #    print(''.join(x))
    res = list()
    for i in range(0, len(a)):
        res.append(''.join(a[i]))
        res.append(''.join(b[i]))
    return res

a = []
while True:
    s = input()
    if not s:
        break
    a.append(list(s))
b = [[' ' for i in range(len(a[0]))] for j in range(len(a))]

# print(func(a, b))
for x in func(a,b):
    print(x)
