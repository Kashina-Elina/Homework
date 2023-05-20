from random import randint
from tkinter import Tk, Button, Label, Entry, Toplevel


class Choice:
    def __init__(self, master: Tk):
        self.master = master
        self.rand = randint(0, 100)
        print(self.rand)
        self.output = 'Введите число от 0 до 100'
        self.output1 = ''
        self.k = 0
        self.enter_button = Button(master, text='Ввод значения', command=lambda: self.hint(self.guess_entry.get()))
        self.reset_button = Button(master, text='Начать заново', command=lambda: self.reset())
        self.count_button = Button(master, text='Количество попыток', command=lambda: self.count())
        self.guess_entry = Entry(master, width=14)
        self.hint_label = Label(master, text=self.output)
        self.hint_label1 = Label(master, text=self.output1)
        self.hint_label1.grid(row=1, column=1)
        self.hint_label.grid(row=0, column=1)
        self.guess_entry.grid(row=2, column=1)
        self.enter_button.grid(row=4, column=0)
        self.reset_button.grid(row=4, column=1)
        self.count_button.grid(row=4, column=2)

    def hint(self, guess):
        try:
            guess = int(guess)
            if 0 <= guess < 100:
                if guess == self.rand:
                    self.output1 = 'Правильный ответ'
                elif guess < self.rand:
                    self.output1 = 'Заданное число больше'
                elif guess > self.rand:
                    self.output1 = 'Заданное число меньше'
                self.k += 1
            else:
                self.output1 = 'Введите число от 0 до 100'
            self.hint_label1.config(text=self.output1)
            return self.output1
        except ValueError:
            print('Введите число')

    def count(self):
        window = Toplevel(self.master)
        self.count_label1 = Label(window, text='Количесво попыток: ' + str(self.k))
        self.count_label1.grid(row=0, column=0)
        return self.count_label1

    def reset(self):
        self.new_rand = randint(0, 100)
        self.rand = self.new_rand
        self.k = 0
        print(self.rand)
        return self.rand, self.count_label1


root = Tk()
my_gui = Choice(root)
root.mainloop()