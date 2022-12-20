from itertools import*
def main():
    s = input().split()
    list1 = []
    for i in permutations(s):
        if list(i) not in list1:
            list1.append(list(i))
    print(list1)

if __name__=="__main__":
    main()