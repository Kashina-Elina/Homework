from itertools import combinations
def main():
    s = input().split()
    output = list()
    for i in range(1, len(s)+1):
        l = list(combinations(s, i))
        output+=l
    print('Подмножества:',set(output))
    print('Количество подмножеств:',len(output))
if __name__=="__main__":
    main()