from tkinter import *
from abc import ABC
from tkinter import messagebox


class Figure(ABC):

    def draw_figure(self):
        ...


class Window:
    def __init__(self, master: Tk):
        super().__init__()
        self.master = master
        self.window = master
        self.rectangle_button = Button(master, text='Прямоугольник', command=lambda: self.draw('1'), width=15)
        self.square_button = Button(master, text='Квадрат', command=lambda: self.draw('2'), width=15)
        self.triangle_button = Button(master, text='Треугольник', command=lambda: self.draw('3'), width=15)
        self.rectangle_button.grid(row=0, column=0)
        self.square_button.grid(row=0, column=1)
        self.triangle_button.grid(row=0, column=2)

    def draw(self, n_figure):
        self.master1 = Toplevel()
        if n_figure == '1':
            self.coords_a_label = Label(self.master1, text='Введите а')
            self.coords_a_entry = Entry(self.master1)
            self.coords_b_label = Label(self.master1, text='Введите b')
            self.coords_b_entry = Entry(self.master1)
            self.draw_buttton = Button(self.master1, text='Нарисовать',
                                       command=lambda: Rectangle(int(self.coords_a_entry.get()),
                                                                           int(self.coords_b_entry.get())))
            self.coords_a_label.grid(row=0, column=0)
            self.coords_b_label.grid(row=2, column=0)
            self.coords_a_entry.grid(row=0, column=1)
            self.coords_b_entry.grid(row=2, column=1)
            self.draw_buttton.grid(row=1, column=2)
        elif n_figure == '2':
            self.coords_a_label = Label(self.master1, text='Введите а')
            self.coords_a_entry = Entry(self.master1)
            self.draw_buttton = Button(self.master1, text='Нарисовать',
                                       command=lambda: Square(int(self.coords_a_entry.get())))

            self.draw_buttton.grid(row=0, column=2)
            self.coords_a_label.grid(row=0, column=0)
            self.coords_a_entry.grid(row=0, column=1)

        elif n_figure == '3':
            self.coords_a_label = Label(self.master1, text='Введите а')
            self.coords_a_entry = Entry(self.master1)
            self.coords_b_label = Label(self.master1, text='Введите h')
            self.coords_b_entry = Entry(self.master1)
            self.draw_buttton = Button(self.master1, text='Нарисовать',
                                       command=lambda: Triangle(int(self.coords_a_entry.get()),
                                                                          int(self.coords_b_entry.get())))
            self.coords_a_label.grid(row=0, column=0)
            self.coords_b_label.grid(row=2, column=0)
            self.coords_a_entry.grid(row=0, column=1)
            self.coords_b_entry.grid(row=2, column=1)
            self.draw_buttton.grid(row=1, column=2)



class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.master2 = Toplevel()
        self.master2.title('Прямоугольник')
        self.draw_figure()
        messagebox.showinfo(title=None, message=self.a * self.b)

    def draw_figure(self):
        canvas = Canvas(self.master2, width=600, height=600)
        canvas.pack()
        canvas.create_rectangle(10, 10, self.a, self.b, outline="blue")



class Square(Figure):
    def __init__(self, a):
        self.a = a
        self.master2 = Toplevel()
        self.master2.title('Квадрат')
        self.draw_figure()
        messagebox.showinfo(title=None, message=self.a * self.a)

    def draw_figure(self):
        canvas = Canvas(self.master2, width=600, height=600)
        canvas.create_rectangle(10, 10, self.a, self.a, fill="white", outline="blue")
        canvas.pack()


class Triangle(Figure):
    def __init__(self, h, a):
        self.h = h
        self.a = a
        self.master2 = Toplevel()
        self.master2.title('Треугольник')
        self.draw_figure()
        messagebox.showinfo(title=None, message=self.a * self.h/2)

    def draw_figure(self):
        canvas = Canvas(self.master2, width=600, height=600)
        points = [10, 10, self.a, self.h / 2, 10, self.h]
        canvas.create_polygon(points, fill='white', outline="blue", width=3)
        canvas.pack()

def main():
    root = Tk()
    f = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()