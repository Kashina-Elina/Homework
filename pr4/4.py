from itertools import product
def main():
    n = int(input())
    output = 0
    output1 = []
    banks = []
    banks1 = []
    for i in range(n):
        k = input().split()
        banks.append(k)
        banks[i][1] = int(banks[i][1])
    l = list(product("01",repeat=n))
    for i in range(len(l)):
        o = ''.join(l[i])
        for j in range(n):
            if '11' not in o:
                c = banks[j][1]*int(o[j])
                output += c
        output1.append([output, o])
        output = 0
    output1.sort(key=lambda x:x[0])
    output1 = list(reversed(output1))
    s = output1[0][1]
    banks1.append(output1[0][0])
    for i in range(n):
        if s[i]=='1':
            banks1.append((banks[i][0], i+1))
    print(banks1)
if __name__ == '__main__':
    main()