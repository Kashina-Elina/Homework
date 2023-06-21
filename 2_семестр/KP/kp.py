import tkinter
from tkinter import messagebox
from ScrollableFrame import *
from typing import Union
from copy import deepcopy
import customtkinter
import pygame as pg
import sys

BLACK = (0, 0, 0)
STATE_BLUE = (106, 90, 205)
LIGHT_YELLOW = (238, 232, 170)
LIGHT_GREEN = (144, 238, 144)
CORAL = (255, 127, 80)
BLUE = (0, 0, 255)


class StartWindow(tkinter.Tk):
    """Класс, создающий стартовое окно ввода данных"""

    def __init__(self):
        """
        v - функция регистрирующая self.validate как функцию, которая будет выполнена при завершении работы программы.
        v1 - функция регистрирующая self.validate_l_k как функцию, которая будет выполнена при завершении работы программы.
        """
        super().__init__()
        v = self.register(self.validate_n)
        v1 = self.register(self.validate_l_k)
        self.entry_n = self.create_label(' введите n ', 0, 0, v)
        self.entry_l = self.create_label(' введите l ', 1, 0, v1)
        self.entry_k = self.create_label(' введите k ', 2, 0, v1)
        Button(self, text='нарисовать', command=lambda: self.create_NewWindow()).grid(row=3, column=0)

    def create_label(self, text_label: str, r: int, c: int, v):
        Label(self, text=text_label).grid(row=r, column=c)
        entry = Entry(self, validate="key", validatecommand=(v, '%P'), width=7)
        entry.grid(row=r, column=1)
        return entry

    @staticmethod
    def validate_n(n: str) -> bool:
        """Метод, проверяющий является ли введённое значение числом и входит ли в диапазон [2, 20]"""
        try:
            if not n:
                return True
            if 0 < int(n) <= 20:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_l_k(self, l: str) -> bool:
        """Метод, проверяющий является ли введённое значение числом"""
        try:
            if not l:
                return True
            if int(l) >= 0 or int(l) <= int(self.entry_n.get()) ** 2:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_coords(self, coords: str) -> tuple:
        """Метод, возвращающий введенные координаты в виде пары x, y"""
        self.coords = coords.split()
        self.x = self.coords[0]
        self.y = self.coords[1]
        return self.x, self.y

    def create_NewWindow(self) -> None:
        """Метод, создающий новое окно"""
        NewWindow(int(self.entry_n.get()), int(self.entry_l.get()), int(self.entry_k.get()))


class NewWindow(tkinter.Tk):
    """Класс, создающий новое окно для воода координат"""

    def __init__(self, n: int, l: int, k: int):
        """
        n, l, k - данные введённые пользователем и отвечающие за размер доски, количество фигур, которые нужно
        расставить, количество фигур, которые уже стоят на доске
        list_figures - список, в котором хранятся экземпляры класса Figure
        scrollable_frame - фрейм с прокруткой
        """
        super().__init__()
        self.n = n
        self.l = l
        self.k = k
        self.list_figures = []
        self.list_for_i = []
        self.geometry('140x200')
        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self, width=130, height=200)
        self.scrollable_frame.pack()
        v1 = self.scrollable_frame.register(self.validate)
        self.visualize(self.k, v1)

    def visualize(self, k, v):
        Label(self.scrollable_frame, text='введите координаты: ').grid(row=0, column=0)
        for i in range(int(k)):
            j = Entry(self.scrollable_frame, validate="key", validatecommand=(v, '%P'), width=7)
            self.list_for_i.append(j)
            j.grid(row=i + 1, column=0)
        Button(self.scrollable_frame, text='нарисовать', command=lambda: self.create_board()).grid(row=k + 1, column=0)

    def validate(self, j: str) -> bool:
        """Метод, проверяющий являются ли два введенных значения числами"""
        try:
            flag = True
            k = j.split()
            for i in k:
                if int(i) < 0 or self.n <= int(i) or j.count(' ') > 1:
                    flag = False
            if flag:
                return True
            else:
                return False
        except ValueError:
            return False

    def func_get_entry(self) -> list:
        """Метод, добавляющий экземпляры класса Figure в список list_figures"""
        for i in self.list_for_i:
            j = Figure(int(i.get().split()[0]), int(i.get().split()[1]), LIGHT_GREEN)
            self.list_figures.append(j)
        return self.list_figures

    def create_board(self) -> None:
        """
        Метод, создающий экземпляр класса Board, осуществляющий проверку заданных фигур на равенство или нахождение
        под боем, а также проверку на отсутствие решений. В случае прохождении проверок вызывает класс DrawBoard,
        который рисует доску с фигурами
        """
        b = Board(self.n, self.l, self.k, self.func_get_entry())
        flag = True
        if len(self.list_figures) > 1:
            for i in self.list_figures:
                for j in self.list_figures:
                    if i != j and j in b.hit(i, True):
                        flag = False
                        messagebox.showinfo(title=None,
                                            message='Фигуры либо равны, либо находятся под боем друг у друга')
                        break
            if flag:
                self.next_window(b)
        else:
            self.next_window(b)

    def next_window(self, b):
        if not b.all_solutions:
            messagebox.showinfo(title=None, message='Нет решений')
        else:
            DrawBoard(self.func_get_entry(), b.all_solutions[0], b.first_solution_hits, self.n, self.l, self.k, b)


class Figure:
    """Класс, создающий фигуру"""

    def __init__(self, x: int, y: int, color: tuple):
        """
        x, y - задают координаты x и y, по которым фигура будет размещена на доске
        color - цвет фигуры
        """
        self.x = x
        self.y = y
        self.color = color

    def search_hit_coords(self, n: int) -> list:
        """Метод, который ищет и добавляет в список координаты клеток, находящиеся под атакой фигур"""
        possible_variants = []
        new_y = self.y - 1
        for j in range(-2, 3, 2):
            new_x = self.x + j
            if 0 <= new_x < n and 0 <= new_y < n:
                possible_variants.append((new_x, new_y))
        new_y = self.y + 1
        for j in range(-2, 3, 2):
            new_x = self.x + j
            if 0 <= new_x < n and 0 <= new_y < n:
                possible_variants.append((new_x, new_y))
        return possible_variants


class Board:
    """Класс, создающий доску"""

    def __init__(self, n: int, l: int, k: int, list_figures: list):
        """
        n, l, k - данные введённые пользователем и отвечающие за размер доски, количество фигур, которые нужно
        расставить, количество фигур, которые уже стоят на доске
        list_figures - список с координатами фигур, введённых пользователем
        """
        self.n = n
        self.l = l
        self.k = k
        self.list_figures = list_figures
        self.board = self.create_board()
        self.all_solutions = []
        self.create_board()
        self.add_figure()
        self.solution_count = 0
        self.first_solution_hits = []
        self.add_new_figure([0, 0], l)
        for i in self.list_figures:
            self.hit(i, True)
        for i in self.board:
            print(*i)

    def create_board(self) -> list:
        """Метод, создающий пустую доску"""
        chess_b = []
        for i in range(self.n):
            str_in_board = []
            for j in range(self.n):
                str_in_board.append('0')
            chess_b.append(str_in_board)
        return chess_b

    def add_figure(self) -> list:
        """Метод, добавляющий фигуры, введенные пользователем из списка list_figures на доску"""
        for i in self.list_figures:
            self.board[i.x][i.y] = '#'
        return self.board

    def hit(self, figure: Figure, flag: bool) -> Union[None, str, list]:
        """Метод, осуществляющий проверку, находится ли фигура под боем"""
        for i in figure.search_hit_coords(self.n):
            if flag:
                self.board[i[0]][i[1]] = '*'
            if not flag:
                if self.board[i[0]][i[1]] == '#':
                    return
        if not flag:
            return 'ok'
        if flag:
            return self.board

    def add_new_figure(self, start: list, l: int) -> list:
        """
        Метод, добавляющий возможные варианты расстановки фигур
        possible_variants - список с координатами, куда может походить фигура
        solution_options - варинаты, куда можно поставить количество фигур, заданное как l
        """
        if l == 0:
            self.solution_count += 1
            figures_coords = []
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == '#':
                        figures_coords.append([i, j])
            if self.solution_count == 1:  # для вывода в консоль первого решения
                new_board = deepcopy(self.board)
                possible_variants = []
                for i in figures_coords:
                    possible_variants += Figure(i[0], i[1], CORAL).search_hit_coords(self.n)
                self.first_solution_hits = possible_variants
                for i in possible_variants:
                    new_board[i[0]][i[1]] = '*'
                for o in new_board:
                    print(o)
            solution = []
            for k in figures_coords:
                if k not in self.list_figures:
                    solution.append(Figure(k[0], k[1], CORAL))
            self.all_solutions.append(solution)
            return figures_coords
        # чтобы при вызове рекурсии функция каждый раз не начинала с 1 элемента
        for i in range(start[0], len(self.board)):
            if i == start[0]:
                for j in range(start[1], len(self.board[i])):
                    if self.board[i][j] == '0' and self.hit(Figure(i, j, BLUE), False) == 'ok':
                        self.board[i][j] = '#'
                        self.add_new_figure([i, j], l - 1)
                        self.board[i][j] = '0'
            else:
                for j in range(len(self.board[i])):
                    if self.board[i][j] == '0' and self.hit(Figure(i, j, BLUE), False) == 'ok':
                        self.board[i][j] = '#'
                        self.add_new_figure([i, j], l - 1)
                        self.board[i][j] = '0'


class DrawBoard:
    """Класс, рисующий доску"""

    def __init__(self, k_coords: list, new_coords: list, hit_variants: list, n: int, l: int, k: int, b: Board):
        """
        k_coords - координаты фигур, введенных пользователем
        new_coords - координаты выставленных программой фигур(первый вариант расстановки)
        hit_variants - возможные варианты, куда может походить фига
        n, l, k - данные введённые пользователем и отвечающие за размер доски, количество фигур, которые нужно
        расставить, количество фигур, которые уже стоят на доске
        b - экземпляр класса Board
        file_out - файл для вывода решений
        RES - размер шахматной доски
        RES1 - размер окна, на которое добавляется шахматная доска
        size - размер каждой клетки доски
        """
        self.file_out = open('output.txt', 'w+', encoding='utf-8')
        self.hit_variants = hit_variants
        self.list_new_coords = new_coords
        self.list_coords = k_coords
        self.RES1 = self.WIDTH, self.HEIGHT = 800, 600
        self.n = n
        self.l = l
        self.k = k
        self.b = b
        self.sc = pg.display.set_mode(self.RES1)
        self.draw()

    def output_to_file(self) -> None:
        """Метод, осуществляющий запись всех вариантов расстановки фигур в файл"""
        variant = self.b.all_solutions
        for k in variant:
            for i in k:
                m = [str(i.x), str(i.y)]
                self.file_out.write(f'({",".join(m)}) ')
            self.file_out.write('\n')
        messagebox.showinfo(title=None, message='Решения записаны в файл')
        self.file_out.close()
        sys.exit()

    def draw(self) -> None:
        """
        Метод, рисующий доску с помощью pygame, а также вызывающий метод output_file для записи в файл решений при
        нажатии на кнопку Output
        """
        RES = self.WIDTH, self.HEIGHT = 600, 600
        FPS = 60
        size = 600 / self.n
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("My Game")
        fontObj = pg.font.Font(None, 48)
        clock = pg.time.Clock()
        text = fontObj.render('Output', True, (0, 0, 0), None)
        outputbutton = (620, 280, 150, 40)
        self.button = pg.draw.rect(self.sc, (255, 255, 255), outputbutton)
        self.sc.blit(text, (630, 290))
        pg.display.update()
        board = pg.Surface(RES)

        for x in range(self.n):
            for y in range(self.n):
                pg.draw.rect(self.sc, LIGHT_YELLOW, [size * x, size * y, size, size])
            pg.display.update()

        for hit in self.hit_variants:
            x, y = hit[0], hit[1]
            pg.draw.rect(self.sc, STATE_BLUE, [size * y, size * x, size, size])
            pg.display.update()
        for new_coords in self.list_new_coords:
            x, y = new_coords.x, new_coords.y
            pg.draw.rect(self.sc, new_coords.color, [size * y, size * x, size, size])
            pg.display.update()
        for coords in self.list_coords:
            x, y = coords.x, coords.y
            pg.draw.rect(self.sc, coords.color, [size * y, size * x, size, size])
            pg.display.update()
        for x in range(self.n):
            for y in range(self.n):
                pg.draw.rect(self.sc, BLACK, [size * x, size * y, size, size], width=2)
                pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button.collidepoint(event.pos):
                            self.output_to_file()

            self.sc.blit(board, (0, 0))


if __name__ == "__main__":
    StartWindow().mainloop()
