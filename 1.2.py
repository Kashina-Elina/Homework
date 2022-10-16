def main():
    x = input()
    y = x[::-1]
    if x[-1]=='0':
        y=x[::-1]
        y=y[1::]
    if x[0]=='-':
        x=x[1::]
        y ='-'+ x[::-1]
    x = int(x)
    y = int(y)
    if  x and y in range(-2**7, 2**7-1, 1):
        print(y)
    else:
        print("no solution")

if __name__ == "__main__":
    main()
