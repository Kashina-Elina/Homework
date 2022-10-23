def main(s, k):
    if k == 0:
        return
    if k == 1:
        print(s, end='')
        return
    for i in range(0, len(s), (k - 1) * 2):
        print(s[i], end='')
    for j in range(1, k - 1):
        down = True
        i = j
        while i < len(s):
            print(s[i], end='')
            if down:
                i += (k - j - 1) * 2
            else:
                i += (k - 1) * 2 - (k - j - 1) * 2
            down = not down
    for i in range(k - 1, len(s), (k - 1) * 2):
        print(s[i], end='')


if __name__ == '__main__':
    k = int(input())
    s = input()
    main(s, k)
