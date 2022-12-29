def func(s):
    rim = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            result += rim.get(s[i])
            i += 1
        elif rim.get(s[i]) >= rim.get(s[i+1]):
            result += rim.get(s[i])
            i += 1
        else:
            result += rim.get(s[i+1])-rim.get(s[i])
            i += 2
    return result
def main():
    print(func(input()))
if __name__ == "__main__":
    main()