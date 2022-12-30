def sweets(n, k):
    if n == k or k == 1:
        return 1
    if k == 0:
        return 0
    else:
        return k*sweets(n-1, k) + sweets(n-1, k-1)
def main():
    list1 = input().split()
    list2 = list(map(int, list1))
    candies = list2[0]
    packages = list2[1]
    if packages > candies:
        print('No solution')
    else:
        print(sweets(candies, packages))
if __name__ == "__main__":
    main()