from tkinter import *
from tkinter import messagebox
from ScrollableFrame import *
import customtkinter
import pygame as pg
import sys


class StartWindow:
    """Класс, создающий стартовое окно ввода данных"""
    def __init__(self, master: 'Tk'):
        """
        master - окно, на которое добавлется текст, поля ввода и кнопки
        v1 - функция регистрирующая self.validateN как функцию, которая будет выполнена при завершении работы программы.
        v2 - функция регистрирующая self.validateL как функцию, которая будет выполнена при завершении работы программы.
        v2 - функция регистрирующая self.validateK как функцию, которая будет выполнена при завершении работы программы.
        draw_button - кнопка, при нажатии на которую вызывается функция создания нового окна
        """
        self.master = master
        v1 = master.register(self.validateN)
        v2 = master.register(self.validateL)
        v3 = master.register(self.validateK)
        self.label1 = Label(master, text='введите n')
        self.label2 = Label(master, text='введите l')
        self.label3 = Label(master, text='введите k')
        self.entry_n = Entry(master, validate="key", validatecommand=(v1, '%P'), width=7)
        self.entry_l = Entry(master, validate="key", validatecommand=(v2, '%P'), width=7)
        self.entry_k = Entry(master, validate="key", validatecommand=(v3, '%P'), width=7)
        self.draw_button = Button(master, text='нарисовать', command=lambda: self.create_NewWindow())
        self.entry_n.grid(row=0, column=1)
        self.label1.grid(row=0, column=0)
        self.entry_l.grid(row=1, column=1)
        self.label2.grid(row=1, column=0)
        self.entry_k.grid(row=2, column=1)
        self.label3.grid(row=2, column=0)
        self.draw_button.grid(row=3, column=0)

    def validateN(self, n):
        """Метод, проверяющий является ли введённое значение числом и входит ли в диапазон [2, 20]"""
        try:
            if not n:
                return True
            if 1<int(n)<=20:
                return True
            else:
                return False
        except ValueError:
            return False

    def validateL(self, l):
        """Метод, проверяющий является ли введённое значение числом"""
        try:
            if not l:
                return True
            if int(l):
                return True
            else:
                return False
        except ValueError:
            return False

    def validateK(self, k):
        """Метод, проверяющий является ли введённое значение числом"""
        try:
            if not k:
                return True
            if int(k):
                return True
            else:
                return False
        except ValueError:
            return False


    def get_coords(self, coords):
        """Метод, возвращающий введенные координаты в виде пары x, y"""
        self.coords = coords.split()
        self.x = self.coords[0]
        self.y = self.coords[1]
        return self.x, self.y

    def create_NewWindow(self):
        """Метод, создающий новое окно"""
        NewWindow(int(self.entry_n.get()), int(self.entry_l.get()),int(self.entry_k.get()), self.master)


class NewWindow:
    """Класс, создающий новое окно для воода координат"""
    def __init__(self, n, l, k, master: 'Tk'):
        """
        LIGHT_GREEN - задаёт цвет фигуры на зеленый
        n, l, k - данные введённые пользователем и отвечающие за размер доски, количество фигур, которые нужно
        расставить, количество фигур, которые уже стоят на доске
        list_figures - список, в котором хранятся экземпляры класса Figure
        master - окно, на которое добавлется текст, поля ввода и кнопки
        scrollable_frame - фрейм с прокруткой
        draw_button - кнопка, при нажатии на которую рисуется доска с фигурами
        """
        self.LIGHT_GREEN = (144, 238, 144)
        self.n = n
        self.l = l
        self.k = k
        self.list_figures = []
        self.list_for_i = []
        self.master = master
        self.new_master = Toplevel(master)
        self.new_master.geometry('140x200')
        self.scrollable_frame = customtkinter.CTkScrollableFrame(master=self.new_master, width=130, height=200)
        self.scrollable_frame.pack()
        self.coords_label = Label(self.scrollable_frame, text='введите координаты: ')
        self.coords_label.grid(row=0, column=0)
        v1 = self.scrollable_frame.register(self.validateJ)
        for i in range(int(k)):
            j = Entry(self.scrollable_frame, validate="key", validatecommand=(v1, '%P'), width=7)
            self.list_for_i.append(j)
            j.grid(row=i+1, column=0)
        self.draw_button = Button(self.scrollable_frame, text='нарисовать', command=lambda: self.create_Board())
        self.draw_button.grid(row=k+1, column=0)

    def validateJ(self, j):
        """Метод, проверяющий являются ли два введенных значения числами"""
        try:
            flag = True
            k = j.split()
            for i in k:
                if int(i) < 0 or self.n <= int(i) or j.count(' ')>1:
                    flag = False
            if flag:
                return True
            else:
                return False
        except ValueError:
            return False

    def func_get_entry(self):
        """Метод, добавляющий экземпляры класса Figure в список list_figures"""
        for i in self.list_for_i:
            j = Figure(i.get().split()[0], i.get().split()[1], self.LIGHT_GREEN)
            self.list_figures.append(j)
        return self.list_figures

    def create_Board(self):
        """
        Метод, создающий экземпляр класса Board, осуществляющий проверку заданных фигур на равенство или нахождение
        под боем, а также проверку на отсутствие решений. В случае прохождении проверок вызывает класс DrawBoard,
        который рисует доску с фигурами
        """
        b = Board(self.n, self.l, self.k, self.func_get_entry())
        if len(self.list_figures) > 1:
            for i in self.list_figures:
                for j in self.list_figures:
                    if i == j or j in b.hit(i, True):
                        messagebox.showinfo(title=None, message='Фигуры либо равны, либо находятся под боем друг у друга')
                    break
                else:
                    if b.solution_options == []:
                        messagebox.showinfo(title=None, message='Нет решений')
                    else:
                        DrawBoard(self.func_get_entry(), b.solution_options[0], b.p_v, self.n, self.l, self.k, self.master, b)

        else:
            if b.solution_options == []:
                messagebox.showinfo(title=None, message='Нет решений')
            else:
                DrawBoard(self.func_get_entry(), b.solution_options[0], b.p_v, self.n, self.l, self.k, self.master, b)


class Figure:
    """Класс, создающий фигуру"""
    def __init__(self, x, y, color):
        """
        x, y - задают координаты x и y, по которым фигура будет размещена на доске
        color - цвет фигуры
        """
        self.x = int(x)
        self.y = int(y)
        self.color = color

    def possible(self, n):
        """Метод, добавляющий в список possible_variants варианты возможных ходов фигур"""
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
    def __init__(self, n, l, k, list_figures):
        """
        n, l, k - данные введённые пользователем и отвечающие за размер доски, количество фигур, которые нужно
        расставить, количество фигур, которые уже стоят на доске
        CORAL - задаёт красный цвет
        list_figures - список с координатами фигур, введённых пользователем
        """
        self.CORAL = (255, 127, 80)
        self.n = n
        self.l = l
        self.k = k
        self.list_figures = list_figures
        self.chess_b = []
        self.solution_options = []
        self.create_board()
        self.add_figure()
        self.count_line = 0
        self.p_v = []
        self.add_new_figure([0, 0], l)
        for i in self.list_figures:
            self.hit(i, True)
        for i in self.chess_b:
            print(*i)


    def create_board(self):
        """Метод, создающий пустую доску"""
        for i in range(self.n):
            str_in_board = []
            for j in range(self.n):
                str_in_board.append('0')
            self.chess_b.append(str_in_board)

    def add_figure(self):
        """Метод, добавляющий фигуры, введеныые пользователем из списка list_figures на доску"""
        for i in self.list_figures:
            self.chess_b[i.x][i.y] = '#'
        return self.chess_b

    def hit(self, figure, flag):
        """Метод, осуществляющий проверку, находится ли фигура под боем"""
        for i in figure.possible(self.n):
            if flag:
                self.chess_b[i[0]][i[1]] = '*'
            if not flag:
                if self.chess_b[i[0]][i[1]] == '#':
                    return
        if not flag:
            return 'ok'
        if flag:
            return self.chess_b

    def add_new_figure(self, start, l):
        """
        Метод, добавляющий возможные варианты расстановки фигур
        possible_variants - список с координатами, куда может походить фигура
        solution_options - варинаты, куда можно поставить количество фигур, заданное как l
        """
        if l == 0:
            self.count_line += 1
            variant = []
            new_board = self.chess_b
            for i in range(len(self.chess_b)):
                for j in range(len(self.chess_b[i])):
                    if self.chess_b[i][j] == '#':
                        variant.append([i, j])
            if self.count_line == 1:  # для вывода в консоль первого решения
                possible_variants = []
                for i in variant:
                    y = i[1] - 1
                    for j in range(-2, 3, 2):
                        x = i[0] + j
                        if 0 <= x < self.n and 0 <= y < self.n:
                            possible_variants.append((x, y))
                    y = i[1] + 1
                    for j in range(-2, 3, 2):
                        x = i[0] + j
                        if 0 <= x < self.n and 0 <= y < self.n:
                            possible_variants.append((x, y))
                self.p_v = possible_variants
                for i in possible_variants:
                    new_board[i[0]][i[1]] = '*'
                for o in new_board:
                    print(o)
            solution_options_1 = []
            for k in variant:
                if k not in self.list_figures:
                    solution_options_1.append(Figure(k[0], k[1], self.CORAL))
            self.solution_options.append(solution_options_1)
            return variant
        # # чтобы при вызове рекурсии функция каждый раз не начинала с 1 элемента
        for i in range(start[0], len(self.chess_b)):
            if i == start[0]:
                for j in range(start[1], len(self.chess_b[i])):
                    if self.chess_b[i][j] == '0' and self.hit(Figure(i, j, (0, 0, 255)), False) == 'ok':
                        self.chess_b[i][j] = '#'
                        self.add_new_figure([i, j], l-1)
                        self.chess_b[i][j] = '0'
            else:
                for j in range(len(self.chess_b[i])):
                    if self.chess_b[i][j] == '0' and self.hit(Figure(i, j, (0, 0, 255)), False) == 'ok':
                        self.chess_b[i][j] = '#'
                        self.add_new_figure([i, j], l-1)
                        self.chess_b[i][j] = '0'



class DrawBoard:
    """Класс, рисующий доску"""
    def __init__(self, k_coords, new_coords, hit_variants, n, l, k, master, b):
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
        BLACK, STATE_BLUE, BLEDZOLOT - черный, синий и светло-желтый цвета
        """
        self.file_out = open('output.txt', 'w+', encoding='utf-8')
        self.master = master
        self.hit_variants = hit_variants
        self.list_new_coords = new_coords
        self.list_coords = k_coords
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.RES1 = self.WIDTH, self.HEIGHT = 800, 600
        self.n = n
        self.l = l
        self.k = k
        self.b = b
        self.sc = pg.display.set_mode(self.RES1)
        self.BLACK = (0,0,0)
        self.STATE_BLUE = (106, 90, 205)
        self.BLEDZOLOT = (238, 232, 170)
        self.FPS = 60
        self.size = 600/self.n
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("My Game")
        self.fontObj = pg.font.Font(None, 48)
        self.clock = pg.time.Clock()
        self.create_pgBoard()

    def output_file(self):
        """Метод, осуществляющий запись всех вариантов расстановки фигур в файл"""
        variant = self.b.solution_options
        for k in variant:
            for i in k:
                m = [str(i.x), str(i.y)]
                self.file_out.write(f'({",".join(m)}) ')
            self.file_out.write('\n')
        return

    def create_pgBoard(self):
        """
        Метод, рисующий доску с помощью pygame, а также вызывающий метод output_file для записи в файл решений при
        нажатии на кнопку Output
        """
        Text = self.fontObj.render('Output', True, (0, 0, 0), None)
        outputButton = 620, 280, 150, 40
        self.button = pg.draw.rect( self.sc, (255, 255, 255), outputButton)
        self.sc.blit(Text, (630, 290))
        pg.display.update()
        board = pg.Surface(self.RES)

        for x in range(self.n):
            for y in range(self.n):
                pg.draw.rect(self.sc, self.BLEDZOLOT, [self.size * x, self.size * y, self.size, self.size])
            pg.display.update()

        for hit in self.hit_variants:
            x, y = hit[0], hit[1]
            pg.draw.rect(self.sc, self.STATE_BLUE, [self.size * y, self.size * x, self.size, self.size])
            pg.display.update()
        for new_coords in self.list_new_coords:
            x, y = new_coords.x, new_coords.y
            pg.draw.rect(self.sc, new_coords.color, [self.size*y, self.size*x, self.size, self.size])
            pg.display.update()
        for coords in self.list_coords:
            x, y = coords.x, coords.y
            pg.draw.rect(self.sc, coords.color, [self.size*y, self.size*x, self.size, self.size])
            pg.display.update()
        for x in range(self.n):
            for y in range(self.n):
                pg.draw.rect(self.sc, self.BLACK, [self.size * x, self.size * y, self.size, self.size], width=2)
                pg.display.update()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button.collidepoint(event.pos):
                            self.output_file()

            self.sc.blit(board, (0, 0))


root = Tk()
my_gui = StartWindow(root)
root.mainloop()