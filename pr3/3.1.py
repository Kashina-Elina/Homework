from itertools import*
def main():
    n=int(input())
    list1 = [int(input()) for _ in range(n)]
    aim = int(input())
    list2 = []
    for i in combinations(list1,4):
        if list(i) not in list2:
            list2.append(list(i))
    minim = abs(sum(list2[0])-aim)
    output1 = list2[0]
    output2 = sum(list2[0])
    for j in range(1,len(list2)):
        k = abs(sum(list2[j])-aim)
        if k<minim:
            minim = k
            output1 = list2[j]
            output2 = sum(list2[j])
    print(output1)
    print(output2)
if __name__=="__main__":
    main()