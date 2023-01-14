def main():
    x = ' '.join(input().split())
    n = len(x)
    flag = False
    maxlen = ''
    for k in range(n):
        if flag:
            break
        new_x = x
        for j in range(len(x)):
            if flag:
                break
            open = ''
            for i in range(len(x)):
                if x[i] in '([{':
                    open += x[i]
                else:
                    if x[i] == ')':
                        if open.endswith('('):
                            open = open[:-1]
                        else:
                            break
                    if x[i] == ']':
                        if open.endswith('['):
                            open = open[:-1]
                        else:
                            break
                    if x[i] == '}':
                        if open.endswith('{'):
                            open = open[:-1]
                        else:
                            break
            else:
                if open == '' and len(x) == n:
                    flag = True
                if open == '':
                    if len(x) > len(maxlen):
                        maxlen = x
            x = x[:-1]
        x = new_x[1:]

    if len(maxlen)==0:
        print('False')
    elif flag:
        print('True')
    else:
        print(maxlen)


if __name__ == "__main__":
    main()
