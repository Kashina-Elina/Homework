def main():
    list1 = input().split()
    list2 = ["".join(sorted(i))for i in list1]
    rez = []
    while len(list1) != 0:
        rez.append([list1[0]])
        list3 = [0]
        for i in range(1, len(list1)):
            if list2[i]==list2[0]:
                rez[-1]+=[list1[i]]
                list3.append(i)
        for i in range(len(list3)):
            del list1[list3[i] - i]
            del list2[list3[i] - i]
    print(rez)
if __name__=="__main__":
    main()