from itertools import combinations
def main():
    s = input().split()
    output = set()
    for i in range(1, len(s)+1):
        l = set(combinations(s, i))
        output.update(l)
    print('Подмножества:',output)
    print('Количество подмножеств:',len(output))
if __name__=="__main__":
    main()