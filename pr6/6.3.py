from itertools import product
def get_pins(a):
    k = []
    output = []
    var = {'1':['1', '2', '4', '-', '-'],
           '2':['2', '1', '5', '3', '-'],
           '3':['3', '2', '6', '-', '-'],
           '4':['4', '1', '5', '7', '-'],
           '5':['5', '4', '2', '6', '8'],
           '6':['6', '3', '5', '9', '-'],
           '7':['7', '4', '8', '-', '-'],
           '8':['8', '7', '5', '9', '0'],
           '9':['9', '8', '6', '-', '-'],
           '0':['0', '8', '-', '-', '-']}
    l = list(product('01234', repeat = len(a)))
    for i in a:
        k.append(var.get(i))
    for i in range(len(l)):
        o = ''.join(l[i])
        s = ''
        for j in range(len(o)):
            s += k[j][int(o[j])]
            if '-' in s:
                break
        else:
            output.append(s)
    return output
def main():
    kod = input()
    print(get_pins(kod))
if __name__ == "__main__":
    main()