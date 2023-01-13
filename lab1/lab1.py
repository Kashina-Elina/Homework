def signs(numbers: list, count: int, current_sum: int, sign: list, need_sum: int) -> list:
    if need_sum == current_sum and count == 0:
        return sign
    if need_sum != current_sum and count == 0:
        return []
    return (signs(numbers[1:], count - 1, current_sum + numbers[0], sign + ['+'], need_sum) or
            signs(numbers[1:], count - 1, current_sum - numbers[0], sign + ['-'], need_sum))

def main():
    file = open('lab1.txt', 'r+', encoding='utf-8')
    c = [int(i) for i in file.read().split()]
    k = len(c)-1
    n = c[0]  # количество чисел
    s = c[-1]  # числа
    c = c[1:k]  # сумма
    rez = ''
    sign = signs(c[1:], len(c)-1, c[0], [], s)
    for i in range(len(c)):
        c[i] = str(c[i])
    for i in range(0,len(sign)):
        rez += c[i] + sign[i]
    rez+=c[-1]+'='+str(s)
    if len(sign)>0:
        file.write('\n'+rez)
    else:
        file.write('\nno solution')
    file.close()
if __name__=="__main__":
    main()