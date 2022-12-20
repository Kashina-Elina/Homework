def main():
    my_set1 = set(input().split())
    my_set2 = set(input().split())

    ans1 = my_set1.intersection(my_set2)
    ans2 = my_set1.symmetric_difference(my_set2)
    ans3 = my_set1.difference(my_set2)
    ans4 = my_set2.difference(my_set1)
    print(len(ans1),'элемента :', *ans1)
    print(len(ans2), 'элементов :', *ans2)
    print(len(ans3), 'элементов :', *ans3)
    print(len(ans4), 'элементов :', *ans4)
if __name__=="__main__":
    main()