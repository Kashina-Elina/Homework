from tkinter import *

class Figure(Frame):
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
            self.draw_buttton = Button(self.master1, text='Нарисовать', command=lambda: self.draw_rectangle(self.coords_a_entry.get(), self.coords_b_entry.get()))
            self.coords_a_label.grid(row=0, column=0)
            self.coords_b_label.grid(row=2, column=0)
            self.coords_a_entry.grid(row=0, column=1)
            self.coords_b_entry.grid(row=2, column=1)
            self.draw_buttton.grid(row=1, column=2)
        elif n_figure == '2':
            self.coords_a_label = Label(self.master1, text='Введите а')
            self.coords_a_entry = Entry(self.master1)
            self.draw_buttton = Button(self.master1, text='Нарисовать', command=lambda: self.draw_square(self.coords_a_entry.get()))
            self.draw_buttton.grid(row=0, column=2)
            self.coords_a_label.grid(row=0, column=0)
            self.coords_a_entry.grid(row=0, column=1)
        elif n_figure == '3':
            self.coords_a_label = Label(self.master1, text='Введите а')
            self.coords_a_entry = Entry(self.master1)
            self.coords_b_label = Label(self.master1, text='Введите b')
            self.coords_b_entry = Entry(self.master1)
            self.draw_buttton = Button(self.master1, text='Нарисовать',
                                       command=lambda: self.draw_triangle(self.coords_a_entry.get(),
                                                                           self.coords_b_entry.get()))
            self.coords_a_label.grid(row=0, column=0)
            self.coords_b_label.grid(row=2, column=0)
            self.coords_a_entry.grid(row=0, column=1)
            self.coords_b_entry.grid(row=2, column=1)
            self.draw_buttton.grid(row=1, column=2)

    def draw_rectangle(self, a, b):
        a = int(a)
        b = int(b)
        self.master2 = Toplevel()
        self.master2.title('Работа с canvas')
        canvas = Canvas(self.master2, width=600, height=600)
        canvas.create_rectangle(10, 10, a, b, fill="white", outline="blue")
        canvas.pack()
    def draw_square(self, a):
        a = int(a)
        self.master2 = Toplevel()
        self.master2.title('Работа с canvas')
        canvas = Canvas(self.master2, width=600, height=600)
        canvas.create_rectangle(10, 10, a, a, fill="white", outline="blue")
        canvas.pack()
    def draw_triangle(self, a, b):
        self.master2 = Toplevel()
        self.master2.title('Работа с canvas')
        canvas = Canvas(self.master2, width=600, height=600)
        canvas_width = int(a)
        canvas_height = int(b)
        points = [10, 10, canvas_width, canvas_height / 2, 10, canvas_height]
        canvas.create_polygon(points, fill='white', outline="blue", width=3)

        canvas.pack()

def main():
    root = Tk()
    f = Figure(root)
    root.mainloop()


if __name__ == '__main__':
    main()
