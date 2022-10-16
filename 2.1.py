def main():
    s = input()
    k = []
    m = []
    for i in range(0, len(s)-1):
        if s[i] != s[i + 1]:
            k.append(s[i])
            if len(m) < len(k):
                m = k
        else:
            k = []
    if s[-2]!=s[-1]:
        k.append(s[-1])
    l="".join(m)
    print(l)
if __name__ == "__main__":
    main()