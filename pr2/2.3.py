def main():
    x = ' '.join(input().split())
    open = ''
    startchar = 0
    maxlen = ''
    for i in range(len(x)):
        if x[i] in '([{':
            open+=x[i]
        else:
            if x[i]==')':
                if open.endswith('('):
                    open= open[:-1]
                else:
                    open = ''
                    startchar=i+1
            if x[i]==']':
                if open.endswith('['):
                    open= open[:-1]
                else:
                    open = ''
                    startchar = i + 1
            if x[i]=='}':
                if open.endswith('{'):
                    open= open[:-1]
                else:
                    open = ''
                    startchar = i + 1
        if len(x[startchar:i+1])>len(maxlen):
            maxlen=x[startchar:i+1]
            if len(maxlen)%2==1:
                maxlen = maxlen[1:]
    if startchar==0:
        print('true')
    else:
        print('false', maxlen)

if __name__=="__main__":
    main()