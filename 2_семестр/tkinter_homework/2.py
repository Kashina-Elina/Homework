from tkinter import Tk, Toplevel, Button, Entry, Label

class ForList:
    def __init__(self, master: Tk):
        self.master = master
        master.title("list")
        self.create_list_button = Button(master, text='создание списка', command=lambda: self.create('1'))
        self.output_button = Button(master, text='вывод списка в консоль', command=lambda: print(self.list1))
        self.write_file_button = Button(master, text='запись данных в файл',command=lambda: self.write_file())
        self.count_list_button = Button(master, text='количество элементов в списке', command=lambda: self.create('2'))
        self.add_elem_button = Button(master, text='добавление элемента в список', command=lambda: self.create('3'))
        self.search_elem_button = Button(master, text='поиск элемента', command=lambda: self.create('4'))
        self.del_elem_button = Button(master, text='удаление элемента', command=lambda: self.create('5'))
        self.exit_button = Button(master, text='выход', command=lambda: self.quit())
        self.create_list_button.grid(row=0, column=0)
        self.output_button.grid(row=0, column=1)
        self.write_file_button.grid(row=1, column=0)
        self.count_list_button.grid(row=1, column=1)
        self.add_elem_button.grid(row=2, column=0)
        self.search_elem_button.grid(row=2, column=1)
        self.del_elem_button.grid(row=3, column=0)
        self.exit_button.grid(row=3, column=1)


    def create_list(self, s):
        self.list1 = s.split()
        return self.list1
    def write_file(self):
        with open('file.txt', 'w') as f:
            self.s = ','.join(self.list1)
            f.write(self.s)
    def add_elem(self, elem):
        self.list1.append(elem)
        return self.list1
    def search(self, elem):
        if elem in self.list1:
            return print('элемент есть в списке')
        else:
            return print('элемента в списке нет')
    def del_elem(self, elem):
        self.list1.remove(elem)
        return self.list1
    def quit(self):
        self.master.destroy()


    def create(self, window):
        if window == '1':
            window1 = Toplevel(self.master)
            window1.title('создание списка')
            self.entry = Entry(master=window1, width=50)
            self.save_button = Button(master=window1, text='сохранить', command=lambda: self.create_list(self.entry.get()))
            self.entry.grid(row=0, column=0)
            self.save_button.grid(row=0, column=1)
        elif window == '2':
            window2 = Toplevel(self.master)
            window2.title('количество элементов списка')
            self.label = Label(master=window2, text=len(self.list1))
            self.label.grid(row=0, column=0)
        elif window == '3':
            window3 = Toplevel(self.master)
            window3.title('добавление элемента')
            self.entry = Entry(master=window3, width=10)
            self.add_button = Button(master=window3, text='добавить', command=lambda: self.add_elem(self.entry.get()))
            self.entry.grid(row=0, column=0)
            self.add_button.grid(row=0, column=1)
        elif window == '4':
            window4 = Toplevel(self.master)
            window4.title('поиск элемента')
            self.entry = Entry(master=window4, width=10)
            self.add_button = Button(master=window4, text='найти', command=lambda: self.search(self.entry.get()))
            self.entry.grid(row=0, column=0)
            self.add_button.grid(row=0, column=1)
        elif window == '5':
            window5 = Toplevel(self.master)
            window5.title('удаление элемента')
            self.entry = Entry(master=window5, width=10)
            self.add_button = Button(master=window5, text='удалить', command=lambda: self.del_elem(self.entry.get()))
            self.entry.grid(row=0, column=0)
            self.add_button.grid(row=0, column=1)

root = Tk()
my_gui = ForList(root)
root.mainloop()