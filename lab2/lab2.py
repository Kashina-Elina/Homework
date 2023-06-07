from copy import deepcopy
count_line = 0


def main():
    file_in = open('input.txt', 'r', encoding='utf-8')
    file_out = open('output.txt', 'r+', encoding='utf-8')
    nlk = [int(i) for i in file_in.readline().split()]
    n = nlk[0]
    l = nlk[1]
    k = nlk[2]
    coordinates = []
    for i in range(k):
        coordinates.append(tuple(int(i) for i in file_in.readline().split()))
    board = chess_board(n)
    add_figure(coordinates, board)
    hit(coordinates, board, n, True)
    new_coordinates = []
    for j in range(len(board)):
        for k in range(len(board[j])):
            coordinates0 = []
            if board[j][k] == '0':
                coordinates0.append(j)
                coordinates0.append(k)
                new_coordinates.append(coordinates0)
    add_new_figure(new_coordinates, board, l, n, [0, 0], file_out)
    if count_line == 0:
        file_out.write('no solution')
    file_in.close()
    file_out.close()


# функция создаёт шахматную доску размером n x n и заполняет ее '0'
def chess_board(n: input) -> list:
    chess_b = []
    for i in range(n):
        board = []
        for j in range(n):
            board.append('0')
        chess_b.append(board)
    return chess_b


# функция добавляет фигуры на доску, обозначая их '#'
def add_figure(coordinate: list, board: list) -> list:
    for i in coordinate:
        x = i[0]
        y = i[1]
        board[x][y] = '#'
    return board


# в  зависимости от флага функция либо расставляет '*' на доступный ход фигуры, либо проверяет, находится ли фигура
# под боем
def hit(coordinate: list, board: list, n: int, flag: bool):
    possible_variants = []
    for i in coordinate:
        y = i[1]-1
        for j in range(-2, 3, 2):
            x = i[0] + j
            if 0 <= x < n and 0 <= y < n:
                possible_variants.append((x, y))
        y = i[1]+1
        for j in range(-2, 3, 2):
            x = i[0] + j
            if 0 <= x < n and 0 <= y < n:
                possible_variants.append((x, y))
    for i in possible_variants:
        if flag:
            board[i[0]][i[1]] = '*'
        if not flag:
            if board[i[0]][i[1]] == '#':
                return
    if not flag:
        return 'ok'
    if flag:
        return board


# функция, которая расставляет новые фигуры на поле
def add_new_figure(coordinate: list, board: list, l: int, n: int, start: list, file_out):
    global count_line
    if l == 0:
        count_line += 1
        variant = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '#':
                    variant.append([i, j])
        if count_line == 1:  # для вывода в консоль первого решения
            new_board = deepcopy(board)
            possible_variants = []
            for i in variant:
                y = i[1] - 1
                for j in range(-2, 3, 2):
                    x = i[0] + j
                    if 0 <= x < n and 0 <= y < n:
                        possible_variants.append((x, y))
                y = i[1] + 1
                for j in range(-2, 3, 2):
                    x = i[0] + j
                    if 0 <= x < n and 0 <= y < n:
                        possible_variants.append((x, y))
            for i in possible_variants:
                new_board[i[0]][i[1]] = '*'
            for o in new_board:
                print(o)
        for k in variant:  # запись всех вариантов расстановки фигур в файл output.txt
            l = list(map(str, k))
            file_out.write(f'({",".join(l)}) ')
        file_out.write('\n')
        return
    # чтобы при вызове рекурсии функция каждый раз не начинала с 1 элемента
    for i in range(start[0], len(board)):
        if i == start[0]:
            for j in range(start[1], len(board[i])):
                if board[i][j] == '0' and hit([[i, j]], board, n, False) == 'ok':
                    board[i][j] = '#'
                    add_new_figure(coordinate, board, l-1, n, [i, j], file_out)
                    board[i][j] = '0'
        else:
            for j in range(len(board[i])):
                if board[i][j] == '0' and hit([[i, j]], board, n, False) == 'ok':
                    board[i][j] = '#'
                    add_new_figure(coordinate, board, l-1, n, [i, j], file_out)
                    board[i][j] = '0'


if __name__ == '__main__':
    main()
