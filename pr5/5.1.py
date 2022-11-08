def main():
    list1 = input().split()
    list2 = input().split()
    ans1=[]
    ans2=[]
    ans3=[]
    ans4=[]
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i]==list2[j]:
                ans1.append(list1[i])
        if list1[i] not in list2:
            ans3.append(list1[i])
            ans2.append(list1[i])
    for j in range(0, len(list2)):
        if list2[j] not in list1:
            ans2.append(list2[j])
            ans4.append(list2[j])
    print(len(ans1), ' :' , ans1)
    print(len(ans2) , ' :' , ans2)
    print(len(ans3) , ' :' , ans3)
    print(len(ans4) , ' :' , ans4)
if __name__=="__main__":
    main()