def santa_users(a):
    for i in a:
        if len(i) < 2:
            i.append(None)
    dict1 = dict(a)
    return dict1
def main():
    n = int(input())
    list1 = []
    for i in range(n):
        s = input().split()
        list1.append(s)
    print(santa_users(list1))

if __name__=="__main__":
    main()